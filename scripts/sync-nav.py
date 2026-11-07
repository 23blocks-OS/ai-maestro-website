#!/usr/bin/env python3
"""Write partials/nav.html, the one site header, into every page in place of its <nav>...</nav>.
Run after editing the partial: python3 scripts/sync-nav.py   (--check: exit 1 if a page differs, change nothing)"""
import pathlib, re, sys

root = pathlib.Path(__file__).resolve().parent.parent
nav = (root / 'partials' / 'nav.html').read_text().strip('\n')
check = '--check' in sys.argv
stale = []
for page in sorted([*root.glob('*.html'), *root.glob('blog/*.html')]):
    html = page.read_text()
    new, n = re.subn(r'[ \t]*<nav\b.*?</nav>', lambda _: nav, html, count=1, flags=re.S)
    if n and new != html:
        stale.append(page.relative_to(root))
        if not check: page.write_text(new)
print(('out of date: ' if check else 'updated: ') + (', '.join(map(str, stale)) or 'none'))
sys.exit(1 if check and stale else 0)
