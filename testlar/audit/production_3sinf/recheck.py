from pathlib import Path
R=Path.cwd();src=(R/'audit/tekshir.py').read_text(encoding='utf-8').replace("str(p.relative_to(ROOT))","p.relative_to(ROOT).as_posix()").replace("str(folder.relative_to(ROOT))","folder.relative_to(ROOT).as_posix()").replace("ROOT.glob('*-sinf')","ROOT.glob('3-sinf')")
ns={'__name__':'grade_three','__file__':str(R/'audit/tekshir.py')};exec(compile(src,'tekshir.py','exec'),ns)
ns['OUT']=R/'audit/production_3sinf/recheck';ns['OUT'].mkdir(exist_ok=True);ns['main']()
