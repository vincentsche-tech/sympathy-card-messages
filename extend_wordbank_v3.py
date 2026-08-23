#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sympathy 词库扩展 v0.3：新增 son/daughter/brother/sister 4 个关系 + meaningful/simple 语气页数据"""
import json

BASE = '/sandbox/workspace/sympathy-site'

NEW_RELATIONSHIPS = {
    "son": {
        "label": "Loss of Son",
        "intro": "Losing a son is one of the most devastating losses a parent can face — it is losing a child, a future, a piece of your heart. When writing, keep it gentle, brief, and free of clichés. Your presence matters more than your words.",
        "messages": {
            "warm": [
                "I am so deeply sorry for the loss of your son. No parent should have to bear this. I'm holding you in my heart.",
                "There are no words for losing a child. Please know I'm here for you, today and in the long days ahead.",
                "I was so heartbroken to hear about your son. He was a wonderful young man, and I know how much he meant to you.",
                "My heart goes out to you and your family. I can't imagine what you're going through, but you don't have to go through it alone."
            ],
            "short": [
                "I am so sorry for the loss of your son.",
                "My heart breaks for you and your family.",
                "No words, just love. I'm so sorry.",
                "Thinking of you and your precious son."
            ],
            "meaningful": [
                "A son is a promise of the future, and losing him is losing that promise. But the love you gave him — that was real, and it was everything. I'm so sorry.",
                "The bond between a parent and child is the deepest there is, and losing a son is a loss that words cannot hold. I'm holding space for you and your family.",
                "Your son was loved, and that love is eternal. I'm so deeply sorry for your unimaginable loss.",
                "There is no timeline for this grief, and there shouldn't be. Take all the time you need, and know I'm here."
            ],
            "religious": [
                "I am so deeply sorry. May God wrap you and your family in His comfort that surpasses all understanding. 'The Lord is close to the brokenhearted' (Psalm 34:18).",
                "Praying for you and your family as you grieve your precious son. May you find peace in God's loving arms.",
                "May the God of all comfort hold you through this unimaginable loss. You are in my prayers."
            ]
        },
        "advice": "Keep it brief and gentle — parents grieving a child are often overwhelmed, and long messages can be too much to process. Acknowledge the loss plainly ('I'm so sorry for the loss of your son'), share one memory if you knew him, and offer concrete help with specifics. Most importantly: keep showing up weeks and months later, when the world has moved on but their grief hasn't.",
        "avoid": "NEVER say 'he's in a better place', 'at least you have other children', 'time heals all wounds', or 'be strong'. Avoid any silver linings — there are none for a parent who lost a child. Don't avoid them either; silence after a child's death is devastatingly common and painful."
    },
    "daughter": {
        "label": "Loss of Daughter",
        "intro": "Losing a daughter is losing a child, a future, a light. It is an unimaginable grief that deserves the gentlest words — or sometimes no words at all, just presence. When writing, keep it simple, honest, and free of any attempt to explain or fix.",
        "messages": {
            "warm": [
                "I am so deeply sorry for the loss of your daughter. She was a light in this world, and I know how much she meant to you.",
                "There are no words for losing a child. Please know I'm here for you, today and in the days ahead.",
                "I was so heartbroken to hear about your daughter. She was a beautiful soul, and I'm holding you in my thoughts.",
                "My heart goes out to you and your family. I'm here, and I'm not going anywhere."
            ],
            "short": [
                "I am so sorry for the loss of your daughter.",
                "My heart breaks for you and your family.",
                "No words, just love. I'm so sorry.",
                "Thinking of you and your precious daughter."
            ],
            "meaningful": [
                "A daughter carries a piece of her parents forever, and losing her leaves a space that nothing can fill. But her light lives on in every life she touched. I'm so deeply sorry.",
                "There is no grief like a parent's grief for their child. I cannot fix this, but I can be here. I'm so sorry for your unimaginable loss.",
                "Your daughter was so loved, and that love is eternal. I'm holding you and your family in my heart.",
                "Grief like this has no schedule. Take every moment you need, and know that I am here — today, next month, next year."
            ],
            "religious": [
                "I am so deeply sorry. May God hold you and your family close. 'He heals the brokenhearted' (Psalm 147:3). You are in my prayers.",
                "Praying for your family as you grieve your precious daughter. May you find comfort in God's eternal love.",
                "May the Lord be your strength and your refuge in this unimaginable time. You are not alone."
            ]
        },
        "advice": "Keep it brief and gentle. Parents grieving a child are in shock — short, sincere messages are easier to hold onto. If you knew her, share one specific memory of her light or laughter. Offer concrete help ('I can bring dinner Thursday'). And most of all, keep showing up: the second month, the first birthday without her, the holidays — that's when presence matters most.",
        "avoid": "Never say 'she's in a better place', 'God needed another angel', or 'at least you can try again'. Avoid 'time heals' and 'be strong'. Never avoid them out of discomfort — silence after losing a child is one of the most painful things a parent experiences."
    },
    "brother": {
        "label": "Loss of Brother",
        "intro": "Losing a brother is losing a childhood companion, a protector, a rival, a friend — someone who shared your history in a way no one else can. When writing, acknowledge the unique bond of siblings and the memories they shared.",
        "messages": {
            "warm": [
                "I am so deeply sorry for the loss of your brother. The bond you shared was special, and I know how much you'll miss him.",
                "Your brother was so much more than a sibling — he was your friend, your history, your person. I'm so sorry.",
                "I was so saddened to hear about your brother. The memories you two shared are a treasure no one can take away.",
                "Siblings share a bond like no other. I'm holding you in my thoughts during this difficult time."
            ],
            "short": [
                "I'm so sorry about your brother. He was special.",
                "Thinking of you. Losing a brother is so hard.",
                "My heart goes out to you and your family.",
                "So sorry for your loss. I'm here for you."
            ],
            "meaningful": [
                "A brother is the only person who shares your childhood — the same house, the same memories, the same inside jokes. Losing him is losing a witness to your life. I'm so deeply sorry.",
                "Brothers may argue, but the bond underneath is unbreakable. His place in your story can never be filled. I'm so sorry.",
                "The memories you made together — the laughter, the mischief, the loyalty — those are his legacy, and they live on in you. I'm so sorry for your loss.",
                "Losing a brother is losing a piece of your own history. I'm holding you and your family in my heart."
            ],
            "religious": [
                "I'm so sorry for your loss. May God comfort you and your family. 'The Lord is close to the brokenhearted' (Psalm 34:18).",
                "Praying for peace and strength for you as you grieve your brother. He is at rest in God's care.",
                "May you find comfort in your faith and in the memories of your brother. You are in my prayers."
            ]
        },
        "advice": "Acknowledge the sibling bond specifically — it's a unique relationship that deserves recognition. If you knew him, share a memory of them together. Offer to listen; grief for a sibling is often under-recognized, so validating it matters. Check in on birthdays and anniversaries — those days are hard.",
        "avoid": "Avoid 'he lived a full life' or comparing losses. Don't say 'you still have your other siblings' — it minimizes this specific loss. Never ask how he died. Don't expect them to 'be strong for their parents' — they're grieving too."
    },
    "sister": {
        "label": "Loss of Sister",
        "intro": "Losing a sister is losing a confidante, a co-conspirator, a mirror of your own history. Sisters share a bond that's part friendship, part rivalry, part unconditional love. When writing, honor that unique connection.",
        "messages": {
            "warm": [
                "I am so deeply sorry for the loss of your sister. The bond you shared was beautiful, and I know how much you'll miss her.",
                "Your sister was your confidante, your partner in everything. I'm so sorry, and I'm holding you in my heart.",
                "I was so saddened to hear about your sister. The memories you shared are a gift that will stay with you forever.",
                "Sisters share a connection like no other. I'm thinking of you and your family."
            ],
            "short": [
                "I'm so sorry about your sister. She was wonderful.",
                "Thinking of you. Losing a sister is so hard.",
                "My heart goes out to you and your family.",
                "So sorry for your loss. I'm here for you."
            ],
            "meaningful": [
                "A sister is your first friend and your forever friend — the keeper of your secrets and your memories. Losing her is losing a part of your story. I'm so deeply sorry.",
                "The bond between sisters is woven through a lifetime of shared moments — laughter, tears, inside jokes. That fabric of love remains. I'm so sorry.",
                "Your sister's love lives on in every memory, every story, every time you hear her laugh in your head. I'm holding you in my heart.",
                "Sisters are the roots of who we become. Losing yours is a profound loss, and I'm so deeply sorry."
            ],
            "religious": [
                "I'm so sorry for your loss. May God comfort you and your family during this difficult time. You are in my prayers.",
                "Praying for peace and strength as you grieve your sister. She is at rest in God's loving care.",
                "May you find comfort in your faith and in the beautiful memories of your sister. You are not alone."
            ]
        },
        "advice": "Honor the sister bond — the confidante relationship, the shared history. If you knew her, share a memory of the two of them together. Offer to listen; sibling grief is often under-acknowledged, and validating it helps. Keep checking in — sibling loss stays with you for life.",
        "avoid": "Avoid 'she's in a better place' unless you know their beliefs. Don't compare losses or say 'at least you have your other siblings.' Never ask how she died. Don't expect them to be 'strong for mom and dad.'"
    }
}

# 语气页数据（meaningful / simple 汇总页）
STYLE_DATA = {
    "meaningful": {
        "label": "Meaningful Condolence Messages",
        "intro": "Some losses ask for more than a simple 'I'm sorry.' These meaningful condolence messages acknowledge the depth of grief and the permanence of love. Use them when you want to say something that truly honors the loss.",
        "messages": {
            "warm": [],
            "short": [],
            "meaningful": [
                "Some losses leave a mark that never fully fades, and that's okay — it means the love was real. I'm so sorry for your loss, and I'm here for you.",
                "Grief is the price we pay for love, and your love for them was clearly immense. I'm holding you in my thoughts.",
                "The people we love never truly leave us — they live on in every memory, every story, every moment we carry them with us. Your loved one lives on in you.",
                "There is a sacredness in grief — it is love that has nowhere to go. I'm so sorry for your loss, and I'm holding your family in my heart.",
                "A mother's love is the first love we ever know, and losing that is losing a part of yourself. But her love is still in you — in the way you care for others, in every lesson she taught you.",
                "Our fathers are often the quiet heroes of our lives — the ones who taught us what it means to be brave, honest, and kind. Your father gave you those gifts, and they live on in you.",
                "A marriage is a life built together — every memory, every milestone, every ordinary Tuesday. Losing your partner is losing a part of that shared life. I'm holding all of it with you.",
                "Friends are the family we choose, and losing one is losing a witness to your life — someone who knew your story and loved you through it.",
                "A brother is the only person who shares your childhood — the same house, the same memories, the same inside jokes. Losing him is losing a witness to your life.",
                "A sister is your first friend and your forever friend — the keeper of your secrets and your memories. Losing her is losing a part of your story.",
                "Pets ask for nothing but love and give everything back. They were a constant — through good days and hard days. Losing them leaves a real emptiness.",
                "Grandmothers are the roots of our family trees — the ones who remember where we came from and love us unconditionally. Their love is eternal.",
                "Grandfathers are the storytellers and the quiet mentors — the ones who taught us patience, hard work, and how to laugh. Their wisdom lives on in you."
            ],
            "religious": []
        },
        "advice": "Meaningful messages work best when they're personal — pair a thoughtful line with a specific memory. These messages acknowledge the permanence of love, which comforts more than any platitude. Read them aloud before sending; sincerity is everything.",
        "avoid": "Avoid pairing meaningful messages with clichés like 'everything happens for a reason' — it undercuts the depth. Don't over-editorialize; let the message breathe. If you're close to the person, consider a handwritten card for maximum impact."
    },
    "simple": {
        "label": "Simple Condolence Messages",
        "intro": "Sometimes the simplest words are the most powerful. These simple condolence messages are short, sincere, and appropriate for any loss — perfect for texts, quick notes, or when you don't know the family well.",
        "messages": {
            "warm": [
                "I'm so sorry for your loss.",
                "Thinking of you during this difficult time.",
                "My deepest sympathy to you and your family.",
                "Sending you love and strength.",
                "My heart is with you.",
                "So sorry to hear this. I'm here for you."
            ],
            "short": [
                "I'm so sorry for your loss.",
                "Thinking of you.",
                "My heart is with you.",
                "Sending you love.",
                "I'm here for you.",
                "So sorry. I'm thinking of you."
            ],
            "meaningful": [],
            "religious": [
                "You are in my prayers.",
                "May God comfort you and your family.",
                "Praying for peace and strength for you."
            ]
        },
        "advice": "Simple doesn't mean cold — a short, sincere message with one personal line is perfect. 'I'm so sorry for your loss. Thinking of you and your family.' is a complete message. If you can, add one small memory: 'I'll never forget how kind she was.' That's the difference between simple and forgettable.",
        "avoid": "Don't pad simple messages with clichés ('he's in a better place') — it defeats the purpose. Don't apologize for being brief; brevity is a kindness when someone is grieving. Avoid adding questions ('how did it happen?') to a simple message."
    }
}

# 合并
with open(f'{BASE}/wordbank.json', encoding='utf-8') as f:
    wb = json.load(f)

for key, data in NEW_RELATIONSHIPS.items():
    wb[key] = data
    print(f'✅ 新增关系: {key} ({data["label"]})')

# 新增 style_pages 段
wb['style_pages'] = STYLE_DATA
print('✅ 新增 style_pages: meaningful/simple')

wb['meta']['version'] = '0.3'
wb['meta']['note'] = wb['meta']['note'].replace('v0.2', 'v0.3').replace('十套', '十四套')

with open(f'{BASE}/wordbank.json', 'w', encoding='utf-8') as f:
    json.dump(wb, f, ensure_ascii=False, indent=2)

rels = [k for k in wb if isinstance(wb[k], dict) and 'messages' in wb[k]]
total = sum(len(wb[k]['messages'].get(t, [])) for k in rels for t in ['warm','short','meaningful','religious'])
print(f'\n🎉 词库 v0.3 完成：{len(rels)} 个关系/风格集，共 {total} 条消息')
