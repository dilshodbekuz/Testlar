import json,shutil
from pathlib import Path
R=Path.cwd();f=R/'4-sinf/4-sinf 4-Sinf Odobnoma';p=f/'_TOLIQ.json';b=R/'audit/production_known_fixes/backup'/p.relative_to(R);b.parent.mkdir(parents=True,exist_ok=True)
if not b.exists():shutil.copy2(p,b)
d=[json.loads(x.read_text(encoding='utf-8')) for x in sorted(f.glob('[0-9]*.json'))];p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
src=(R/'audit/tekshir.py').read_text(encoding='utf-8').replace('str(p.relative_to(ROOT))','p.relative_to(ROOT).as_posix()').replace('str(folder.relative_to(ROOT))','folder.relative_to(ROOT).as_posix()')
ns={'__name__':'current_audit','__file__':str(R/'audit/tekshir.py')};exec(compile(src,'tekshir.py','exec'),ns);ns['OUT']=R/'audit/production_known_fixes/recheck';ns['OUT'].mkdir(exist_ok=True);ns['main']()
