import re, json, glob, os, html

def html_unescape(s):
    return html.unescape(s)

EXCLUDE = ('test/', 'scripts/')
files = sorted(
    f for f in glob.glob('**/*.html', recursive=True)
    if not any(x in f for x in EXCLUDE) and '"@type": "FAQPage"' in open(f, encoding='utf-8').read()
)

total_miss = 0
problem_pages = []
for fn in files:
    c = open(fn, encoding='utf-8').read()
    # 1) parse FAQPage JSON-LD
    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', c, flags=re.S)
    qa_ld = {}
    for b in blocks:
        try:
            d = json.loads(b)
        except Exception:
            continue
        if isinstance(d, dict) and d.get('@type') == 'FAQPage':
            for e in d['mainEntity']:
                qa_ld[e['name'].strip()] = e['acceptedAnswer']['text'].strip()
    # 2) extract visible faq-item: <div class="faq-item"><b>Q</b><p>A</p></div>
    items = re.findall(r'<div class="faq-item">\s*<b>(.*?)</b>\s*<p>(.*?)</p>', c, flags=re.S)
    vis_clean = []
    for q, a in items:
        q = re.sub(r'<[^>]+>', '', q)
        a = re.sub(r'<[^>]+>', '', a)
        q = html_unescape(q).strip()
        a = html_unescape(a).strip()
        a = re.sub(r'\s+', ' ', a)
        q = re.sub(r'\s+', ' ', q)
        vis_clean.append((q, a))
    miss = 0
    for q, a in vis_clean:
        if q not in qa_ld:
            print(f'  [{fn}] Q MISS: {q[:60]!r}')
            miss += 1
            continue
        if qa_ld[q] != a:
            # show diff preview
            print(f'  [{fn}] A DIFF for {q[:45]!r}')
            print(f'      LD : {qa_ld[q][:80]!r}')
            print(f'      VIS: {a[:80]!r}')
            miss += 1
    if miss:
        problem_pages.append(fn)
    total_miss += miss
    print(f'{fn:48} visible={len(vis_clean):2} jsonld={len(qa_ld):2} | MISS={miss}')

print('-' * 80)
print(f'TOTAL MISS: {total_miss} across {len(files)} FAQ pages')
if problem_pages:
    print('PROBLEM PAGES:', problem_pages)
else:
    print('ALL FAQ PAGES CONSISTENT (0 mismatch)')
