#!/usr/bin/env python3
"""
sympathy 站加厚：grandmother + grandfather 各加 3 个 .card 教学块
- 关系页用"该避免什么"原型（不能套礼物逻辑）
- 3 块：When to Send / Card vs Text vs In-Person / What to Avoid (deeper)
- 插入点：'How to Write' 卡之后、'More Sympathy Message Guides' 网格之前
- 目标：grandmother 767→~965 / grandfather 724→~930（精准 +200 词）
- 每块 2 段紧凑结构，每块 ~70 词
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).parent.parent

# Grandmother 块（每块 2 段 ~70 词 = +210 总）
GUIDE_BLOCKS = {
    'condolence-messages-for-loss-of-grandmother.html': """
  <div class="card">
    <h2>When to Send the Card (and the Window That Matters)</h2>
    <p>There is no perfect moment, but there is a meaningful window. Within the first two weeks, your message becomes part of the family's first days of grief. After the first month, a card still matters: it tells the bereaved they are not forgotten.</p>
    <p><b>Three timing windows.</b> The first week: a short note that says "I'm so sorry" is enough. Weeks two to four: a longer card with a specific memory of grandmother (her laugh, her recipe, the way she said your name) becomes a keepsake. After the first month: the overlooked window — send a one-line card that acknowledges their ongoing grief. Survivors remember that sentence for years. If grandmother passed weeks ago and you haven't sent anything — send now.</p>
  </div>

  <div class="card">
    <h2>Card vs. Text vs. In-Person: Picking the Right Medium</h2>
    <p>How you deliver the message matters as much as what you say. The bereaved will read your message many times; the medium signals how much you meant it.</p>
    <p><b>Card</b> when you knew her personally or have a specific memory to share — cards are keepsakes, survivors return to them for years. <b>Text</b> when you want to acknowledge quickly and follow up with a card later — texts are disposable but survivors screenshot the ones that matter. <b>In-person</b> when you knew her well and the family is close to you — but only if you can be present without making the moment about your own grief.</p>
  </div>

  <div class="card">
    <h2>What to Avoid (A Deeper List)</h2>
    <p>The obvious "what to avoid" is well-known: don't say "they're in a better place" without knowing their beliefs, don't make it about your own grandmother, don't ask about the will. Here are the quieter mistakes worth knowing.</p>
    <p><b>Phrases that sound helpful but hurt.</b> "At least you had her for so long" minimizes the loss even when her life was long. "Time heals everything" doesn't — it just changes the shape. "She's with grandpa now" — don't assume the family finds comfort in that framing without knowing their beliefs. When you don't know what to say, the line that almost always works is: "I don't know what to say, but I want you to know I'm thinking of you."</p>
  </div>
""",
    'condolence-messages-for-loss-of-grandfather.html': """
  <div class="card">
    <h2>When to Send the Card (and the Window That Matters)</h2>
    <p>There is no perfect moment, but there is a meaningful window. Within the first two weeks, your message becomes part of the family's first days of grief. After the first month, a card still matters: it tells the bereaved they are not forgotten.</p>
    <p><b>Three timing windows.</b> The first week: a short note that says "I'm so sorry" is enough. Weeks two to four: a longer card with a specific memory of grandfather (his workshop, his joke, the way he taught you something) becomes a keepsake. After the first month: the overlooked window — send a one-line card that acknowledges their ongoing grief. For the quiet ones who loved a quiet man, that one sentence arrives at exactly the moment it matters.</p>
  </div>

  <div class="card">
    <h2>Card vs. Text vs. In-Person: Picking the Right Medium</h2>
    <p>How you deliver the message matters as much as what you say. The bereaved will read your message many times; the medium signals how much you meant it.</p>
    <p><b>Card</b> when you knew him personally or have a specific memory to share — cards are keepsakes, survivors return to them for years. <b>Text</b> when you want to acknowledge quickly and follow up with a card later — texts are disposable but survivors screenshot the ones that matter. <b>In-person</b> when you knew him well and the family is close to you — but only if you can be present without making the moment about your own grief.</p>
  </div>

  <div class="card">
    <h2>What to Avoid (A Deeper List)</h2>
    <p>The obvious "what to avoid" is well-known: don't say "they're in a better place" without knowing their beliefs, don't make it about your own grandfather, don't ask about the will. Here are the quieter mistakes worth knowing.</p>
    <p><b>Phrases that sound helpful but hurt.</b> "At least he lived a full life" minimizes the loss even when his life was full. "Time heals everything" doesn't — it just changes the shape. "He was tough — he'd want you to be tough too" makes grief a contest, when grieving openly is not weakness. When you don't know what to say, the line that almost always works is: "I don't know what to say, but I want you to know I'm thinking of you."</p>
  </div>
""",
}


def count_visible(c):
    t = re.sub(r'<style.*?</style>', '', c, flags=re.S)
    t = re.sub(r'<script.*?</script>', '', t, flags=re.S)
    t = re.sub(r'<head.*?</head>', '', t, flags=re.S)
    t = re.sub(r'<[^>]+>', ' ', t)
    t = re.sub(r'&[a-z]+;', ' ', t)
    t = re.sub(r'\s+', ' ', t)
    return len(t.split())


def insert_guide(c, block):
    more_marker = '<h2>More Sympathy Message Guides</h2>'
    more_pos = c.find(more_marker)
    if more_pos < 0:
        return c, False
    before_more = c.rfind('<div class="card">', 0, more_pos)
    if before_more < 0:
        return c, False
    return c[:before_more] + block + '\n' + c[before_more:], True


def is_idempotent(c):
    return 'A Deeper List' in c


def main():
    dry = '--dry' in sys.argv
    import json
    for fn, block in GUIDE_BLOCKS.items():
        fp = ROOT / fn
        if not fp.exists():
            print(f'SKIP {fn}')
            continue
        c = fp.read_text(encoding='utf-8')
        before_wc = count_visible(c)
        if is_idempotent(c):
            print(f'{fn}: ALREADY-INSERTED (skip, before={before_wc})')
            continue
        new_c, ok = insert_guide(c, block)
        if not ok:
            print(f'{fn}: INSERT-FAILED')
            continue
        after_wc = count_visible(new_c)
        delta = after_wc - before_wc
        flag = '' if after_wc >= 800 else '  ⚠️ UNDER 800'
        over_flag = '  ⚠️ OVER 1100' if after_wc > 1100 else ''
        print(f'{fn}: {before_wc}→{after_wc} (+{delta}){flag}{over_flag}')

        # FAQ 严格校验
        blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', new_c, flags=re.S)
        faq = {}
        for b in blocks:
            try:
                ld = json.loads(b)
            except Exception:
                continue
            if isinstance(ld, dict) and ld.get('@type') == 'FAQPage':
                for e in ld['mainEntity']:
                    faq[e['name'].strip()] = e['acceptedAnswer']['text'].strip()
        m = re.search(r'<h2>Frequently Asked Questions</h2>(.*?)</main>', new_c, flags=re.S)
        vis = re.findall(r'<div class="faq-item"><b>(.*?)</b><p>(.*?)</p></div>', m.group(1) if m else '', flags=re.S)
        miss = 0
        for vq, va in vis:
            vq = re.sub(r'\s+', ' ', vq.strip())
            va = re.sub(r'\s+', ' ', va.strip())
            if vq not in faq or faq.get(vq, '') != va:
                miss += 1
        print(f'  FAQ A-MISS={miss}')

        if not dry:
            fp.write_text(new_c, encoding='utf-8')
            print(f'  → wrote')


if __name__ == '__main__':
    main()
