import re, os, html, glob, json

EXCLUDE = ('test/', 'scripts/')
files = sorted(
    f for f in glob.glob('**/*.html', recursive=True)
    if not any(x in f for x in EXCLUDE)
)

print(f"{'file':48} {'title':>5} {'desc':>5} {'3label':>6} {'FAQ':>4} {'visFAQ':>6} {'words':>6}")
print('-' * 110)

def strip_text(c):
    c = re.sub(r'<style.*?</style>', '', c, flags=re.S)
    c = re.sub(r'<script.*?</script>', '', c, flags=re.S)
    c = re.sub(r'<head.*?</head>', '', c, flags=re.S)
    c = re.sub(r'<[^>]+>', ' ', c)
    c = re.sub(r'&[a-z]+;', ' ', c)
    c = re.sub(r'\s+', ' ', c)
    return c.strip()

for fn in files:
    c = open(fn, encoding='utf-8').read()
    mt = re.search(r'<title>(.*?)</title>', c)
    md = re.search(r'<meta name="description" content="(.*?)"', c)
    mog = re.search(r'<meta property="og:title" content="(.*?)"', c)
    mtw = re.search(r'<meta name="twitter:title" content="(.*?)"', c)
    t = html.unescape(mt.group(1)) if mt else 'NO'
    d = md.group(1) if md else 'NO'
    og = html.unescape(mog.group(1)) if mog else 'NO'
    tw = html.unescape(mtw.group(1)) if mtw else 'NO'
    three_sync = (t == og == tw)
    has_faq = '"@type": "FAQPage"' in c
    # count visible FAQ items (try both structures)
    n_details = len(re.findall(r'<details>\s*<summary>(.*?)</summary>', c, flags=re.S))
    n_faqitem = len(re.findall(r'<div class="faq-item">', c))
    n_divfaq = len(re.findall(r'<div class="faq">', c))
    vis = max(n_details, n_faqitem, n_divfaq)
    body = strip_text(c)
    words = len(body.split())
    print(f"{fn:48} {len(t):>5} {len(d):>5} {str(three_sync):>6} {str(has_faq):>4} {vis:>6} {words:>6}")
