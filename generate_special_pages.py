#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""特殊页：religious-condolence-messages + bible-verses-for-loss-of-mother"""
import json

BASE = '/sandbox/workspace/sympathy-site'
DOMAIN = 'https://whatsowriteinasympathycard.com'
GA4 = '''<script async src="https://www.googletagmanager.com/gtag/js?id=G-QBK28ZBRSB"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-QBK28ZBRSB');
</script>'''

HEAD = '''<!DOCTYPE html>
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
  .card h2{{font-size:20px;margin-bottom:14px;}}
  .card h3{{font-size:17px;margin:20px 0 10px;}}
  .msg-item{{display:flex;align-items:flex-start;gap:10px;background:var(--soft);border:1px solid var(--line);border-radius:12px;padding:14px 16px;margin-bottom:10px;}}
  .msg-text{{flex:1;font-size:15px;line-height:1.6;}}
  .msg-copy{{background:var(--accent);color:#fff;border:none;border-radius:8px;padding:6px 12px;font-size:12.5px;font-weight:600;cursor:pointer;white-space:nowrap;flex-shrink:0;}}
  .msg-copy.copied{{background:#6b8f7f;}}
  .verse-item{{background:var(--soft);border:1px solid var(--line);border-radius:12px;padding:18px 20px;margin-bottom:12px;}}
  .verse-item .ref{{font-family:Georgia,serif;font-size:17px;font-weight:700;color:var(--accent-dark);display:block;margin-bottom:6px;}}
  .verse-item .text{{font-style:italic;font-size:15.5px;margin-bottom:8px;color:#4a4742;}}
  .verse-item .use{{font-size:14px;color:#5c5852;}}
  .grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:14px;}}
  .scene-card{{display:block;background:#fff;border:1px solid var(--line);border-radius:12px;padding:18px 20px;text-decoration:none;color:var(--ink);transition:all .15s;}}
  .scene-card:hover{{border-color:var(--accent);box-shadow:var(--shadow);}}
  .scene-card b{{font-size:15px;display:block;margin-bottom:4px;color:var(--accent-dark);}}
  .scene-card span{{font-size:13.5px;color:var(--muted);}}
  .advice-box{{background:var(--soft);border-left:4px solid var(--accent);border-radius:0 10px 10px 0;padding:18px 20px;margin:16px 0;}}
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
      <a href="/religious-condolence-messages.html">Religious</a>
      <a href="/bible-verses-for-loss-of-mother.html">Bible Verses</a>
      <a href="/about.html">About</a>
    </nav>
  </div>
</header>
<main>
'''

FOOT = '''</main>
<footer>
  Copyright <span id="year"></span> © <a href="/">Sympathy Words</a>. Made with care for people in hard times.<br>
  <a href="/about.html">About</a> · <a href="/contact.html">Contact</a> · <a href="/privacy-policy.html">Privacy</a> · <a href="/terms.html">Terms</a>
</footer>
<div class="toast" id="toast"></div>
<script>
document.querySelectorAll('.msg-copy').forEach(function(btn){
  btn.addEventListener('click',function(){
    var text=btn.parentElement.querySelector('.msg-text').textContent;
    function done(){btn.textContent='✓ Copied';btn.classList.add('copied');showToast('Copied! Add your personal memory 💛');setTimeout(function(){btn.textContent='Copy';btn.classList.remove('copied');},1800);gtag('event','message_copied',{});}
    if(navigator.clipboard&&window.isSecureContext){navigator.clipboard.writeText(text).then(done);}
    else{var ta=document.createElement('textarea');ta.value=text;ta.style.position='fixed';ta.style.opacity='0';document.body.appendChild(ta);ta.select();try{document.execCommand('copy');done();}catch(e){}document.body.removeChild(ta);}
  });
});
let toastTimer;
function showToast(msg){var t=document.getElementById('toast');t.textContent=msg;t.classList.add('show');clearTimeout(toastTimer);toastTimer=setTimeout(function(){t.classList.remove('show');},2200);}
document.getElementById('year').textContent=new Date().getFullYear();
</script>
</body>
</html>
'''

SCENE_LINKS = '''      <a class="scene-card" href="/what-to-write-in-a-sympathy-card.html"><b>What to Write in a Card</b><span>The complete guide with 50+ examples.</span></a>
      <a class="scene-card" href="/condolence-messages-for-loss-of-mother.html"><b>Loss of Mother</b><span>Messages that honor a mom's love.</span></a>
      <a class="scene-card" href="/condolence-messages-for-loss-of-father.html"><b>Loss of Father</b><span>Words for losing a dad.</span></a>
      <a class="scene-card" href="/condolence-messages-for-loss-of-husband.html"><b>Loss of Husband</b><span>Messages for a grieving wife.</span></a>
      <a class="scene-card" href="/condolence-messages-for-loss-of-pet.html"><b>Loss of a Pet</b><span>Comfort for losing a companion.</span></a>
      <a class="scene-card" href="/short-condolence-messages.html"><b>Short Messages</b><span>Brief and meaningful, for texts.</span></a>'''

# ============ 页面 1: Religious Condolence Messages ============
wb = json.load(open(f'{BASE}/wordbank.json', encoding='utf-8'))
REL_ORDER = [('general', 'General'), ('mother', 'Loss of Mother'), ('father', 'Loss of Father'),
             ('husband', 'Loss of Husband'), ('wife', 'Loss of Wife'), ('friend', 'Loss of a Friend'),
             ('coworker', 'Loss of a Coworker'), ('grandmother', 'Loss of Grandmother'),
             ('grandfather', 'Loss of Grandfather'), ('pet', 'Loss of a Pet')]

sections = []
for key, label in REL_ORDER:
    msgs = wb[key]['messages'].get('religious', [])
    if not msgs:
        continue
    items = ''.join(f'      <div class="msg-item"><div class="msg-text">{m}</div><button class="msg-copy">Copy</button></div>\n' for m in msgs)
    sections.append(f'    <h3>🙏 For {label}</h3>\n{items}')

religious_body = f'''  <div class="hero">
    <h1>Religious Condolence Messages</h1>
    <p>For families who find comfort in faith, these messages and scripture offer peace and hope. Choose the one that fits the relationship, then add your own warm words.</p>
  </div>
  <div class="card">
    <h2>💌 Faith-Based Sympathy Messages</h2>
    <p style="font-size:14.5px;color:#5c5852;margin-bottom:16px;">Click any message to copy it. All include scripture or faith-centered comfort.</p>
{''.join(sections)}
    <p style="margin-top:16px;font-size:14.5px;">Looking for scripture specifically? See <a href="/bible-verses-for-loss-of-mother.html" style="color:var(--accent);">Bible verses for loss of mother</a> or use the <a href="/" style="color:var(--accent);">free generator</a> for any situation.</p>
  </div>
  <div class="card">
    <h2>How to Write a Religious Condolence Message</h2>
    <div class="advice-box">
      <h3>✅ Do</h3>
      <ul style="margin-left:20px;">
        <li>Match their faith tradition — ask or recall what you know</li>
        <li>Pair scripture with your own warm words, not scripture alone</li>
        <li>Offer specific prayers: "I'm praying for you and your family"</li>
        <li>Say the person's name and acknowledge the loss directly</li>
      </ul>
    </div>
    <div class="advice-box" style="border-left-color:var(--gold);">
      <h3>❌ Don't</h3>
      <ul style="margin-left:20px;">
        <li>Don't assume their beliefs — "he's in a better place" may not fit</li>
        <li>Don't use scripture to explain away the loss or rush their grief</li>
        <li>Don't make it a sermon — keep the focus on them and their loved one</li>
      </ul>
    </div>
  </div>
  <div class="card">
    <h2>More Sympathy Message Guides</h2>
    <div class="grid">
{SCENE_LINKS}
    </div>
  </div>
  <div class="card">
    <h2>Frequently Asked Questions</h2>
    <div class="faq-item"><b>Should I include a Bible verse in a sympathy card?</b><p>If the family is religious, a short verse like Psalm 34:18 or Matthew 5:4 can be deeply comforting. Pair it with your own sincere words — scripture alone can feel impersonal.</p></div>
    <div class="faq-item"><b>What if I don't know their religious beliefs?</b><p>Use a non-religious message, or a gentle phrase like "sending you peace and comfort." You can always say "you're in my prayers" only if you genuinely pray.</p></div>
    <div class="faq-item"><b>What's the best Bible verse for a sympathy card?</b><p>Common choices: Psalm 34:18 ("The Lord is close to the brokenhearted"), Matthew 5:4 ("Blessed are those who mourn"), and Revelation 21:4 ("He will wipe every tear from their eyes").</p></div>
  </div>
'''

# ============ 页面 2: Bible Verses for Loss of Mother ============
VERSES = [
    ("Psalm 34:18", "The Lord is close to the brokenhearted and saves those who are crushed in spirit.",
     "One of the most comforting verses for any loss. Use it when you want to acknowledge that God is near them in their pain — not fixing it, but present in it."),
    ("Matthew 5:4", "Blessed are those who mourn, for they will be comforted.",
     "Jesus' own words. It validates their grief as sacred and promises comfort. Beautiful for a mother's funeral card."),
    ("Psalm 147:3", "He heals the brokenhearted and binds up their wounds.",
     "Gentle and direct. Use when you want to speak hope without rushing their healing."),
    ("Revelation 21:4", "He will wipe every tear from their eyes. There will be no more death or mourning or crying or pain.",
     "Speaks to the promise of a life without loss. Powerful for religious families, especially after a long illness."),
    ("Isaiah 41:10", "So do not fear, for I am with you; do not be dismayed, for I am your God. I will strengthen you and help you; I will uphold you with my righteous right hand.",
     "A verse of strength and presence. Use when you want to offer courage alongside comfort."),
    ("Psalm 23:4", "Even though I walk through the darkest valley, I will fear no evil, for you are with me; your rod and your staff, they comfort me.",
     "The most beloved psalm for grief. It acknowledges the darkness while affirming God's presence through it."),
    ("John 14:27", "Peace I leave with you; my peace I give you. I do not give to you as the world gives. Do not let your hearts be troubled and do not be afraid.",
     "Offers a peace that isn't dependent on circumstances. Use for a message of hope after the funeral."),
    ("2 Corinthians 1:3-4", "Praise be to the God of all comfort, who comforts us in all our troubles, so that we can comfort those in any trouble with the comfort we ourselves receive from God.",
     "A beautiful verse that frames grief as something God walks with us through — and that our comforted hearts can comfort others."),
    ("Psalm 116:15", "Precious in the sight of the Lord is the death of his faithful servants.",
     "Acknowledges that God values her life and her passing. Tender and specific — lovely for a mother."),
    ("Lamentations 3:22-23", "Because of the Lord's great love we are not consumed, for his compassions never fail. They are new every morning; great is your faithfulness.",
     "Speaks of God's mercies that renew daily — hope for the hard days ahead, not just today."),
]

verse_items = ''.join(
    f'    <div class="verse-item"><span class="ref">{ref}</span><div class="text">"{text}"</div><div class="use"><b>How to use it:</b> {use}</div></div>'
    for ref, text, use in VERSES
)

bible_body = f'''  <div class="hero">
    <h1>Bible Verses for Loss of Mother</h1>
    <p>When words fail, scripture can carry comfort. These verses are chosen for someone grieving a mother — each with a note on how to use it in a sympathy card.</p>
  </div>
  <div class="card">
    <h2>📖 Comforting Scripture for Grieving a Mother</h2>
{verse_items}
    <p style="margin-top:16px;font-size:14.5px;">Prefer to write your own message with faith woven in? See <a href="/religious-condolence-messages.html" style="color:var(--accent);">religious condolence messages</a> or use the <a href="/" style="color:var(--accent);">free generator</a>.</p>
  </div>
  <div class="card">
    <h2>How to Include a Bible Verse in a Sympathy Card</h2>
    <div class="advice-box">
      <h3>✅ The Right Way</h3>
      <ul style="margin-left:20px;">
        <li>Pair the verse with your own words: "I'm so sorry about your mother. 'The Lord is close to the brokenhearted' — I'm praying you feel His nearness."</li>
        <li>Choose a verse that fits their mother's faith and their relationship with God</li>
        <li>Keep it to one verse — more can feel overwhelming</li>
      </ul>
    </div>
    <div class="advice-box" style="border-left-color:var(--gold);">
      <h3>❌ Avoid</h3>
      <ul style="margin-left:20px;">
        <li>Using scripture to explain the loss ("it was God's plan") — this rarely comforts</li>
        <li>Verses that imply her death was deserved or purposeful</li>
        <li>Quoting a long passage when a single, meaningful verse will do</li>
      </ul>
    </div>
  </div>
  <div class="card">
    <h2>More Sympathy Message Guides</h2>
    <div class="grid">
{SCENE_LINKS}
    </div>
  </div>
  <div class="card">
    <h2>Frequently Asked Questions</h2>
    <div class="faq-item"><b>What is the best Bible verse for a mother's funeral?</b><p>Psalm 34:18 and Matthew 5:4 are the most common and comforting choices. Psalm 23 is also deeply meaningful for many families. Choose what fits her faith and your relationship with the family.</p></div>
    <div class="faq-item"><b>Should I write the verse myself or use a card?</b><p>Handwrite it if you can, alongside your own words. A verse alone can feel distant; a verse plus one personal line is a gift.</p></div>
    <div class="faq-item"><b>Is it okay to use a Bible verse if the family isn't religious?</b><p>No — respect their beliefs. For families who aren't religious, use a warm, non-faith message instead.</p></div>
  </div>
'''

pages = {
    'religious-condolence-messages.html': {
        'title': 'Religious Condolence Messages – 30+ Faith-Based Examples',
        'desc': 'Faith-based sympathy messages with scripture for religious families. Warm, comforting condolence messages for any loss.',
        'body': religious_body,
    },
    'bible-verses-for-loss-of-mother.html': {
        'title': 'Bible Verses for Loss of Mother – 10 Comforting Scriptures',
        'desc': '10 comforting Bible verses for someone grieving their mother, each with guidance on how to use it in a sympathy card.',
        'body': bible_body,
    },
}

for slug, p in pages.items():
    html = HEAD.format(title=p['title'], desc=p['desc'], domain=DOMAIN, slug=slug.replace('.html',''), ga4=GA4) + p['body'] + FOOT
    with open(f'{BASE}/{slug}', 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'✅ {slug}')
