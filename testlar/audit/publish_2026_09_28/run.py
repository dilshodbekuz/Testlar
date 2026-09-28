from pathlib import Path
root=Path.cwd()
src=(root/'audit/tekshir.py').read_text(encoding='utf-8').replace("str(p.relative_to(ROOT))", "p.relative_to(ROOT).as_posix()").replace("str(folder.relative_to(ROOT))", "folder.relative_to(ROOT).as_posix()")
ns={'__name__':'fresh_audit','__file__':str(root/'audit/tekshir.py')}
exec(compile(src,'tekshir.py','exec'),ns)
ns['OUT']=root/'audit/publish_2026_09_28'
ns['main']()
