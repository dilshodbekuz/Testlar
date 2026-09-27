"""Read-only checks of source tests; writes audit artifacts only.

Automatic checks never substitute for individual semantic review.
"""
from pathlib import Path
from collections import Counter, defaultdict
from fractions import Fraction
import ast
import hashlib
import json
import re
import unicodedata

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'audit/qayta_3sinf'

def dump(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True)

def norm(text):
    return re.sub(r'\s+', ' ', unicodedata.normalize('NFKC', str(text)).translate(str.maketrans({'‘':"'", '’':"'", 'ʻ':"'", 'ʼ':"'"}))).strip().casefold()

def number_expr(text):
    # In school notation '/' is a fraction bar, while ÷ and : divide whole fractions.
    # Preserve fraction operands before translating the outer division signs.
    if ('÷' in text or ':' in text) and '/' in text:
        if re.search(r'\d\s*/\s*\d+\s*/',text):
            raise ValueError('Ambiguous chained fraction')
        text=re.sub(r'(?<![\w./])(\d+\s*/\s*\d+)(?![\w./])',r'(\1)',text)
    text = text.strip().translate(str.maketrans({'−':'-', '–':'-', '×':'*', '·':'*', ':':'/', '÷':'/'}))
    if not re.fullmatch(r'[0-9\s.+*/()\-]+', text) or len(text) > 160 or '**' in text or '//' in text:
        raise ValueError('Not a simple arithmetic expression')
    def visit(node):
        if isinstance(node, ast.Constant) and type(node.value) in (int,float):
            return Fraction(str(node.value))
        if isinstance(node, ast.UnaryOp) and isinstance(node.op,(ast.UAdd,ast.USub)):
            return visit(node.operand) * (-1 if isinstance(node.op,ast.USub) else 1)
        if isinstance(node,ast.BinOp):
            left,right=visit(node.left),visit(node.right)
            if isinstance(node.op,ast.Add): return left+right
            if isinstance(node.op,ast.Sub): return left-right
            if isinstance(node.op,ast.Mult): return left*right
            if isinstance(node.op,ast.Div): return left/right
        raise ValueError('Unsupported expression')
    return visit(ast.parse(text,mode='eval').body)

def arithmetic_question(question):
    patterns=[
        r'^([\d\s.+*/():÷×·−–\-]+)\s+(?:ifodasining qiymati |ifodaning qiymati |ko.paytmasi )?(?:nechaga|nimaga) teng\?$',
        r'^([\d\s.+*/():÷×·−–\-]+)\s+(?:ifodasining qiymatini|ifodaning qiymatini) toping\.?$',
        r'^Ustun shaklida yeching:\s*([\d\s.+*/():÷×·−–\-]+)\s*=\s*\?$',
        r'^(?:Hisoblang:\s*)?([\d\s.+*/():÷×·−–\-]+)\s*=\s*\?$',
        r'^Guruhlab qo.shing:\s*([\d\s.+*/():÷×·−–\-]+)$',
    ]
    for pat in patterns:
        m=re.fullmatch(pat,question.strip(),re.I)
        if m: return number_expr(m.group(1))
    raise ValueError('Outside supported question templates')

def main():
    records=[]; findings=[]; file_issues=[]; all_json={}; folders=defaultdict(list)
    def issue(row,code,detail,certainty='aniq',severity='muhim'):
        item={'file':row['file'],'question_no':row['question_no'],'code':code,'detail':detail,'certainty':certainty,'severity':severity}
        findings.append(item);row['automatic_findings'].append(code)
    for grade in sorted(ROOT.glob('3-sinf')):
        for p in sorted(grade.rglob('*.json')):
            rel=str(p.relative_to(ROOT))
            try: data=json.loads(p.read_text())
            except Exception as e:
                file_issues.append({'file':rel,'code':'json_parse','detail':str(e)});continue
            all_json[rel]=data
            if p.name.startswith('_'):continue
            folders[p.parent].append(p)
            if not isinstance(data,dict) or not isinstance(data.get('savollar'),list):
                file_issues.append({'file':rel,'code':'schema','detail':'savollar ro‘yxati yo‘q'});continue
            txt=p.with_suffix('.txt')
            parsed_txt=[]
            if txt.exists():
                text=txt.read_text()
                blocks=re.split(r'(?m)^(\d+)\. ',text)
                for k in range(1,len(blocks),2):
                    lines=blocks[k+1].splitlines()
                    opts=[]; answers=[]; question_lines=[lines[0]]; reached_options=False
                    for line in lines[1:]:
                        m=re.fullmatch(r'(\+?)([A-D])\) ?(.*)',line)
                        if m:
                            reached_options=True
                            opts.append(m.group(3))
                            if m.group(1):answers.append(ord(m.group(2))-65)
                        elif not reached_options:
                            question_lines.append(line)
                    if opts:
                        parsed_txt.append((int(blocks[k]),'\n'.join(question_lines).rstrip(),opts,answers))
                if len(parsed_txt)!=len(data['savollar']):file_issues.append({'file':rel,'code':'txt_count','detail':f"JSON: {len(data['savollar'])}; TXT: {len(parsed_txt)}"})
            else:file_issues.append({'file':rel,'code':'missing_txt','detail':'TXT nusxa yo‘q'})
            for i,q in enumerate(data['savollar'],1):
                row={'file':rel,'question_no':i,'grade':grade.name,'subject':p.parent.name,'topic':data.get('mavzu'),'question':q,'sha256':hashlib.sha256(dump(q).encode()).hexdigest(),'automatic_checked':True,'automatic_findings':[], 'semantic_status':'tekshirilmagan','arithmetic_status':'qo‘llanilmagan'}
                records.append(row)
                if not isinstance(q,dict): issue(row,'schema','Savol obyekt emas');continue
                s=q.get('savol');v=q.get('variantlar');a=q.get('togri')
                if not isinstance(s,str) or not s.strip():issue(row,'empty_question','Savol matni bo‘sh yoki matn emas')
                if not isinstance(v,list) or len(v)!=4 or any(not isinstance(x,str) or not x.strip() for x in v):issue(row,'options','4 ta bo‘sh bo‘lmagan matn variant talab qilinadi');continue
                if type(a)!=int or not 0<=a<len(v):issue(row,'answer_index','Javob indeksi 0–3 oralig‘ida emas');continue
                groups=defaultdict(list)
                # Case and whitespace are meaningful in genetics, formulas and code outputs.
                # Do not casefold or collapse whitespace when declaring duplicates.
                for j,x in enumerate(v): groups[x].append(j)
                for key,idx in groups.items():
                    if len(idx)>1:issue(row,'duplicate_options',f"Bir xil variantlar: {', '.join('ABCD'[j] for j in idx)} = {v[idx[0]]}" + ('; belgilangan javob ham takrorlangan' if a in idx else ''))
                if any(subject in p.parent.name for subject in ['Matematika','Algebra','Geometriya']):
                    equivalents=defaultdict(list)
                    for j,x in enumerate(v):
                        try: equivalents[str(number_expr(x))].append(j)
                        except (ValueError,SyntaxError,ZeroDivisionError):pass
                    for value,idx in equivalents.items():
                        if len(idx)>1 and len(set(v[j] for j in idx))>1:
                            issue(row,'equivalent_numeric_options',f"Bir xil son qiymati ({value}): {', '.join('ABCD'[j] for j in idx)}; savol aynan kasr shakli yoki yozilishini so‘rasa, bu xato bo‘lmasligi mumkin",'tekshirish_kerak','tekshiruv')
                if q.get('qiyinlik') not in ['oson',"o'rtacha",'qiyin']:issue(row,'difficulty',f"Noma’lum qiyinlik: {q.get('qiyinlik')}")
                if isinstance(s,str):
                    try:
                        expected=arithmetic_question(s)
                        vals=[]; parsed_variants=[]
                        for j,x in enumerate(v):
                            try:
                                parsed_variants.append(j)
                                if number_expr(x)==expected:vals.append(j)
                            except (ValueError,SyntaxError,ZeroDivisionError):parsed_variants.remove(j)
                        row['arithmetic_expected']=str(expected)
                        row['arithmetic_status']='hisoblandi'
                        if a in parsed_variants and a not in vals:issue(row,'arithmetic_wrong',f"Hisoblangan javob: {expected}; belgilangan: {v[a]}; mos variantlar: {','.join('ABCD'[j] for j in vals) or 'yo‘q'}")
                        if len(vals)>1:issue(row,'arithmetic_multiple',f"Qiymati {expected} bo‘lgan variantlar: {','.join('ABCD'[j] for j in vals)}")
                    except (ValueError,SyntaxError,ZeroDivisionError):pass
                    if re.search(r'[àèìòùâêîôûåõÀÈÌÒÙÂÊÎÔÛÅÕ�]',s+' '+' '.join(v)):
                        issue(row,'text_encoding','G‘ayrioddiy lotin belgilari bor; asl matn bilan solishtirish kerak','gumon','tahrir')
                    if re.search(r'\b(matn(?:da|ga|dan|ning)?|rasm(?:da|ga|dagi)?|jadval(?:da|ga|dagi)?|she.r(?:da|ga|dagi)?|hikoya(?:da|ga|dagi)?|muallif|asarda)\b',norm(s)):
                        row['source_context_may_be_needed']=True
                if i<=len(parsed_txt):
                    ti,ts,tv,ta=parsed_txt[i-1]
                    if (ti,ts,tv,ta)!=(i,s,v,[a]): issue(row,'txt_json_difference','TXT va JSON savol matni, variantlari yoki javobi mos emas')
    for grade in sorted(ROOT.glob('3-sinf')):
        for folder in sorted(x for x in grade.iterdir() if x.is_dir()):
            ps=folders[folder];rel=str(folder.relative_to(ROOT))
            if not ps:file_issues.append({'file':rel,'code':'empty_subject','detail':'Alohida mavzu JSON testlari yo‘q'})
            agg=all_json.get(rel+'/_TOLIQ.json')
            if isinstance(agg,list):
                individual=Counter(dump(all_json[str(p.relative_to(ROOT))]) for p in ps)
                combined=Counter(dump(x) for x in agg)
                extras=individual-combined;missing=combined-individual
                if extras or missing:file_issues.append({'file':rel,'code':'aggregate_difference','detail':f'{sum(extras.values())} ta alohida fayl tarkibi jamlanmada yo‘q; {sum(missing.values())} ta jamlanma yozuvi alohida fayllarda yo‘q'})
            elif ps:file_issues.append({'file':rel,'code':'missing_aggregate','detail':'_TOLIQ.json jamlanmasi yo‘q yoki ro‘yxat emas'})
            prefix=defaultdict(list)
            for p in ps:prefix[p.name.split('_')[0]].append(p.name)
            for num,names in prefix.items():
                if len(names)>1:file_issues.append({'file':rel,'code':'duplicate_topic_number','detail':f'{num}: '+ '; '.join(names)})
    review_path=OUT/'manual_reviews.json'
    reviews=json.loads(review_path.read_text()) if review_path.exists() else []
    record_index={(r['file'],r['question_no']):r for r in records}
    for review in reviews:
        row=record_index[(review['file'],review['question_no'])]
        if review.get('sha256') != row['sha256']:raise ValueError('Reviewed question changed: '+review['file'])
        row['semantic_status']=review['status'];row['semantic_notes']=review.get('notes',[])
    with (OUT/'savollar_holati.jsonl').open('w') as f:
        for row in records:f.write(dump(row)+'\n')
    with (OUT/'avtomatik_topilmalar.jsonl').open('w') as f:
        for item in findings:f.write(dump(item)+'\n')
    (OUT/'fayl_muammolari.json').write_text(json.dumps(file_issues,ensure_ascii=False,indent=2)+'\n')
    stats={}
    for grade in sorted(set(r['grade'] for r in records)):
        rs=[r for r in records if r['grade']==grade]
        stats[grade]={'questions':len(rs),'files':len(set(r['file'] for r in rs)),'automatic_flagged':sum(bool(r['automatic_findings']) for r in rs),'arithmetic_calculated':sum(r['arithmetic_status']=='hisoblandi' for r in rs),'semantic_reviewed':sum(r['semantic_status']!='tekshirilmagan' for r in rs),'semantic_pending':sum(r['semantic_status']=='tekshirilmagan' for r in rs)}
    (OUT/'statistika.json').write_text(json.dumps({'grades':stats,'automatic_findings':dict(Counter(x['code'] for x in findings)),'file_findings':dict(Counter(x['code'] for x in file_issues))},ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'grades':stats,'automatic_findings':dict(Counter(x['code'] for x in findings)),'file_findings':dict(Counter(x['code'] for x in file_issues))},ensure_ascii=False,indent=2))

if __name__=='__main__':main()
