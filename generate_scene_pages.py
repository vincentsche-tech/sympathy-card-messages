#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sympathy 站场景页生成：从 wordbank.json 渲染 mother/father 等场景页（5要素：引言+列表+建议+避免+FAQ）"""
import json, os, re

BASE = '/sandbox/workspace/sympathy-site'
DOMAIN = 'https://whatsowriteinasympathycard.com'
GA_TAG = 'G-XXXXXXXXXX'  # TODO: 替换为新 GA4 Measurement ID

wb = json.load(open(f'{BASE}/wordbank.json', encoding='utf-8'))

GA4 = f'''<script async src="https://www.googletagmanager.com/gtag/js?id={GA_TAG}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GA_TAG}');
</script>'''

TONE_META = {
    'warm': ('🤍 Warm & Sincere', 'Thoughtful messages that offer genuine warmth.'),
    'short': ('📝 Short & Simple', 'Brief messages for cards, texts, and quick notes.'),
    'meaningful': ('💭 Meaningful & Thoughtful', 'Deeper messages about love, memory, and grief.'),
    'religious': ('🙏 Religious & Faith-Based', 'Messages with scripture and faith for religious families.'),
}

SCENES = {
    'mother': {
        'slug': 'condolence-messages-for-loss-of-mother',
        'h1': 'Condolence Messages for Loss of Mother',
        'title': 'Condolence Messages for Loss of Mother – 30+ Heartfelt Examples',
        'desc': 'Losing a mother is one of the deepest losses. Find heartfelt condolence messages for loss of mother — warm, short, meaningful, and religious examples.',
        'faq': [
            ('What do you say to someone who lost their mother?',
             'Start with simple sincerity: "I am so sorry for the loss of your mother." Then add one line about her warmth or a memory. Acknowledging her and her role in their life matters more than finding the perfect words.'),
            ('What should I write in a sympathy card for loss of mother?',
             'Acknowledge the loss, express your sorrow, and if you knew her, share a specific memory — "I will never forget how she made everyone feel at home." Offer concrete help with a time attached, like bringing dinner on Tuesday.'),
            ('What not to say when someone\'s mother dies?',
             'Avoid "she\'s in a better place" unless you know their beliefs, and "at least she lived a long life" — it minimizes their grief. Never say "I know how you feel" unless you have truly lost your own mother.'),
            ('How long does grief for a mother last?',
             'There is no timeline. Grief comes in waves and changes over years. What matters is that you keep showing up — a message on Mother\'s Day or the anniversary of her death means more than most people realize.'),
        ],
    },
    'father': {
        'slug': 'condolence-messages-for-loss-of-father',
        'h1': 'Condolence Messages for Loss of Father',
        'title': 'Condolence Messages for Loss of Father – 30+ Heartfelt Examples',
        'desc': 'Losing a father is losing a guide and anchor. Find heartfelt condolence messages for loss of father — warm, short, meaningful, and religious examples.',
        'faq': [
            ('What do you say to someone who lost their father?',
             'Acknowledge his role: "I am so sorry for the loss of your father. He was a steady, kind presence and I know how much he meant to you." A specific memory of him — his humor, his advice, his quiet strength — means the world.'),
            ('What not to say when someone\'s father dies?',
             'Avoid "be strong for your family" or "man up" — it pressures the grieving and shuts down healthy grief. Avoid "time heals all wounds" too soon. Never ask how he died; let them share if they want to.'),
            ('How do I write a sympathy card for loss of father?',
             'Follow the same structure: acknowledge the loss, express sorrow, share a memory or quality, offer specific help, close warmly. If you didn\'t know him well, focus on the person you do know: "I know how much your father meant to you."'),
            ('Should I mention memories of the father?',
             'Yes — sharing one specific memory validates his life and gives comfort like nothing else. "I\'ll always remember how proud he was when he talked about you" is a gift.'),
        ],
    },
}

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{domain}/{slug}.html">
<meta name="theme-color" content="#5b7a6e">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E%F0%9F%95%8A%EF%B8%8F%3C/text%3E%3C/svg%3E">
{ga4}
<style>
  :root{{--bg:#faf8f5;--card:#fff;--ink:#3d3a36;--muted:#8a857d;--accent:#5b7a6e;--accent-dark:#4a655a;--soft:#eef2ef;--line:#e8e4dd;--gold:#c9a86a;--radius:14px;--shadow:0 4px 20px rgba(61,58,54,.06);}}
  *{{margin:0;padding:0;box-sizing:border-box;}}
  body{{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;background:var(--bg);color:var(--ink);line-height:1.7;}}
  h1,h2,h3{{font-family:Georgia,"Times New Roman",serif;font-weight:700;letter-spacing:-.2px;}}
  header{{background:#fff;border-bottom:1px solid var(--line);padding:16px 0;}}
  header .inner{{max-width:960px;margin:0 auto;padding:0 20px;display:flex;align-items:center;gap:14px;flex-wrap:wrap;}}
  .logo{{background:var(--accent);color:#fff;font-family:Georgia,serif;font-size:15px;font-weight:700;padding:7px 14px;border-radius:8px;text-decoration:none;}}
  nav.topnav{{margin-left:auto;display:flex;gap:16px;flex-wrap:wrap;}}
  nav.topnav a{{color:var(--muted);font-size:14px;text-decoration:none;}}
  nav.topnav a:hover{{color:var(--accent);}}
  main{{max-width:960px;margin:0 auto;padding:36px 20px 64px;}}
  .hero{{text-align:center;margin-bottom:28px;}}
  .hero h1{{font-size:31px;line-height:1.25;}}
  .hero p{{color:var(--muted);margin-top:12px;font-size:16px;max-width:640px;margin-left:auto;margin-right:auto;}}
  .card{{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);box-shadow:var(--shadow);padding:28px;margin-bottom:24px;}}
  .card h2{{font-size:20px;margin-bottom:12px;}}
  .card h3{{font-size:17px;margin:20px 0 10px;}}
  .advice-box{{background:var(--soft);border-left:4px solid var(--accent);border-radius:0 10px 10px 0;padding:18px 20px;margin:16px 0;}}
  .advice-box.gold{{border-left-color:var(--gold);}}
  .advice-box h3{{font-size:16px;margin:0 0 8px;}}
  .advice-box ul{{margin-left:20px;}}
  .advice-box li{{margin-bottom:6px;font-size:14.5px;}}
  .msg-item{{display:flex;align-items:flex-start;gap:10px;background:var(--soft);border:1px solid var(--line);border-radius:12px;padding:14px 16px;margin-bottom:10px;}}
  .msg-text{{flex:1;font-size:15px;line-height:1.6;}}
  .msg-copy{{background:var(--accent);color:#fff;border:none;border-radius:8px;padding:6px 12px;font-size:12.5px;font-weight:600;cursor:pointer;white-space:nowrap;flex-shrink:0;}}
  .msg-copy.copied{{background:#6b8f7f;}}
  .grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:14px;}}
  .scene-card{{display:block;background:#fff;border:1px solid var(--line);border-radius:12px;padding:18px 20px;text-decoration:none;color:var(--ink);transition:all .15s;}}
  .scene-card:hover{{border-color:var(--accent);box-shadow:var(--shadow);}}
  .scene-card b{{font-size:15px;display:block;margin-bottom:4px;color:var(--accent-dark);}}
  .scene-card span{{font-size:13.5px;color:var(--muted);}}
  .faq-item{{margin-bottom:18px;}}
  .faq-item b{{display:block;margin-bottom:4px;font-size:15px;}}
  .faq-item p{{font-size:14.5px;color:#5c5852;}}
  footer{{text-align:center;color:var(--muted);font-size:13px;padding:28px 0 48px;border-top:1px solid var(--line);}}
  footer a{{color:var(--accent);text-decoration:none;}}
  .toast{{position:fixed;bottom:24px;left:50%;transform:translateX(-50%) translateY(80px);background:var(--ink);color:#fff;padding:10px 22px;border-radius:999px;font-size:14px;opacity:0;transition:all .3s;pointer-events:none;z-index:99;}}
  .toast.show{{opacity:1;transform:translateX(-50%) translateY(0);}}
  @media(max-width:600px){{.hero h1{{font-size:25px;}}}}
</style>
</head>
<body>
<header>
  <div class="inner">
    <a class="logo" href="/">🕊️ Sympathy Words</a>
    <nav class="topnav">
      <a href="/">Generator</a>
      <a href="/what-to-write-in-a-sympathy-card.html">Card Messages</a>
      <a href="/condolence-messages-for-loss-of-mother.html">Loss of Mother</a>
      <a href="/condolence-messages-for-loss-of-father.html">Loss of Father</a>
      <a href="/about.html">About</a>
    </nav>
  </div>
</header>

<main>
  <div class="hero">
    <h1>{h1}</h1>
    <p>{intro}</p>
  </div>

  <div class="card">
    <h2>💌 {label} Messages</h2>
    <p style="font-size:14.5px;color:#5c5852;margin-bottom:16px;">Click any message to copy it, then add your own personal line to make it yours.</p>
{tone_sections}
    <p style="margin-top:16px;font-size:14.5px;">Need a different situation? Use the <a href="/" style="color:var(--accent);">free sympathy message generator</a> or browse <a href="/what-to-write-in-a-sympathy-card.html" style="color:var(--accent);">more card message guides</a>.</p>
  </div>

  <div class="card">
    <h2>How to Write These Messages Well</h2>
    <div class="advice-box">
      <h3>✅ What to Say</h3>
      <p style="font-size:14.5px;">{advice}</p>
    </div>
    <div class="advice-box gold">
      <h3>❌ What to Avoid</h3>
      <p style="font-size:14.5px;">{avoid}</p>
    </div>
  </div>

  <div class="card">
    <h2>More Sympathy Message Guides</h2>
    <div class="grid">
      <a class="scene-card" href="/what-to-write-in-a-sympathy-card.html"><b>What to Write in a Card</b><span>The complete guide with 50+ examples.</span></a>
      <a class="scene-card" href="/condolence-messages-for-loss-of-mother.html"><b>Loss of Mother</b><span>Messages that honor a mom's love.</span></a>
      <a class="scene-card" href="/condolence-messages-for-loss-of-father.html"><b>Loss of Father</b><span>Words for losing a dad.</span></a>
      <a class="scene-card" href="/short-condolence-messages.html"><b>Short Messages</b><span>Brief and meaningful, for texts.</span></a>
    </div>
  </div>

  <div class="card">
    <h2>Frequently Asked Questions</h2>
{faq}
  </div>
</main>

<footer>
  Copyright <span id="year"></span> © <a href="/">Sympathy Words</a>. Made with care for people in hard times.<br>
  <a href="/about.html">About</a> · <a href="/contact.html">Contact</a> · <a href="/privacy-policy.html">Privacy</a> · <a href="/terms.html">Terms</a>
</footer>

<div class="toast" id="toast"></div>

<script>
document.querySelectorAll('.msg-copy').forEach(function(btn){{
  btn.addEventListener('click',function(){{
    var text=btn.parentElement.querySelector('.msg-text').textContent;
    function done(){{
      btn.textContent='✓ Copied';btn.classList.add('copied');
      showToast('Copied! Add your personal memory 💛');
      setTimeout(function(){{btn.textContent='Copy';btn.classList.remove('copied');}},1800);
      gtag('event','message_copied',{{}});
    }}
    if(navigator.clipboard&&window.isSecureContext){{navigator.clipboard.writeText(text).then(done);}}
    else{{var ta=document.createElement('textarea');ta.value=text;ta.style.position='fixed';ta.style.opacity='0';document.body.appendChild(ta);ta.select();try{{document.execCommand('copy');done();}}catch(e){{}}document.body.removeChild(ta);}}
  }});
}});
let toastTimer;
function showToast(msg){{var t=document.getElementById('toast');t.textContent=msg;t.classList.add('show');clearTimeout(toastTimer);toastTimer=setTimeout(function(){{t.classList.remove('show');}},2200);}}
document.getElementById('year').textContent=new Date().getFullYear();
</script>
</body>
</html>
"""


def build_tone_sections(rel_data):
    out = []
    for tone, (label, sub) in TONE_META.items():
        msgs = rel_data['messages'].get(tone, [])
        if not msgs:
            continue
        items = ''.join(
            f'      <div class="msg-item"><div class="msg-text">{m}</div><button class="msg-copy">Copy</button></div>\n'
            for m in msgs
        )
        out.append(f'    <h3>{label}</h3>\n    <p style="font-size:13.5px;color:var(--muted);margin-bottom:10px;">{sub}</p>\n{items}')
    return '\n'.join(out)


def build_faq(faq_list):
    return '\n'.join(
        f'    <div class="faq-item"><b>{q}</b><p>{a}</p></div>'
        for q, a in faq_list
    )


def main():
    for key, meta in SCENES.items():
        rel = wb[key]
        tone_sections = build_tone_sections(rel)
        faq = build_faq(meta['faq'])
        html = PAGE.format(
            title=meta['title'], desc=meta['desc'], domain=DOMAIN,
            slug=meta['slug'], ga4=GA4, h1=meta['h1'], intro=rel['intro'],
            label=rel['label'], tone_sections=tone_sections,
            advice=rel['advice'], avoid=rel['avoid'], faq=faq,
        )
        path = f"{BASE}/{meta['slug']}.html"
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        total = sum(len(rel['messages'].get(t, [])) for t in TONE_META)
        print(f'✅ {path} ({total} msgs)')


if __name__ == '__main__':
    main()
