#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""扩展 wordbank.json：新增 7 个关系（husband/wife/friend/coworker/grandmother/grandfather/pet）"""
import json

BASE = '/sandbox/workspace/sympathy-site'

NEW_RELATIONSHIPS = {
    "husband": {
        "label": "Loss of Husband",
        "intro": "Losing a husband is losing a partner, a best friend, and a home all at once. When writing, acknowledge the marriage itself — the life they built together. Be gentle, be present, and avoid any suggestion that they 'should' be strong right now.",
        "messages": {
            "warm": [
                "I am so deeply sorry for the loss of your husband. He was a wonderful partner and a dear friend to so many. I'm holding you in my heart.",
                "Your husband was so clearly devoted to you — the way he looked at you said it all. I'm so sorry, and I'm here for you through this.",
                "There are no words for losing the person you built your life with. Please know I'm thinking of you, and I'm here whenever you need me.",
                "I was so saddened to hear about your husband. The love you two shared was evident to everyone who knew you. Sending you all my strength."
            ],
            "short": [
                "I'm so deeply sorry for your loss. He was a wonderful man.",
                "Thinking of you and your family. Your husband will be so missed.",
                "My heart is with you during this unimaginable time.",
                "So sorry for your loss. I'm here for you."
            ],
            "meaningful": [
                "A marriage is a life built together — every memory, every milestone, every ordinary Tuesday. Losing your husband means losing a part of that shared life. I'm so sorry, and I'm holding all of it with you.",
                "The love you shared with your husband doesn't end with his passing — it lives in every story, every habit, every moment you carry him with you. I'm so deeply sorry.",
                "He was your person — the one who knew you best and loved you anyway. That kind of love leaves a mark nothing can erase. I'm so sorry for your loss.",
                "Some people walk into our lives and change everything. Your husband was that for you, and his love will always be part of who you are. I'm holding you in my thoughts."
            ],
            "religious": [
                "May God wrap you in His comfort as you grieve your beloved husband. He is at peace in God's loving arms. You are in my prayers.",
                "I'm so sorry for your loss. 'The Lord is close to the brokenhearted' (Psalm 34:18). May you feel His presence holding you.",
                "Praying for your strength and peace, knowing your husband rests in eternal love. You are not alone."
            ]
        },
        "advice": "Acknowledge the marriage — the life they built together. Say his name and share a memory of him if you can. Offer concrete, ongoing help: grief after losing a spouse is long, so check in weeks and months later, not just right after. Meals, errands, and company are all deeply appreciated.",
        "avoid": "Never suggest 'you're young, you'll find someone again' — it's deeply hurtful. Avoid 'at least you had him for [X] years' — it minimizes their loss. Don't say 'be strong for the kids' — it pressures them to hide their grief."
    },
    "wife": {
        "label": "Loss of Wife",
        "intro": "Losing a wife is losing a partner, a confidante, and the heart of the home. When writing, acknowledge her warmth and the life they built. Men grieving a wife often struggle to ask for help — be specific with your offers.",
        "messages": {
            "warm": [
                "I am so deeply sorry for the loss of your wife. She was a beautiful soul and the heart of your home. I'm thinking of you and your family.",
                "Your wife was so warm and kind — everyone who met her felt it. I'm so sorry for your loss, and I'm here for you.",
                "There are no words for losing the person who was your everything. Please know I'm here, today and in the weeks ahead.",
                "I was so saddened to hear about your wife. The love you shared was clear to everyone. Sending you strength and peace."
            ],
            "short": [
                "I'm so deeply sorry for your loss. She was a wonderful woman.",
                "Thinking of you. Your wife will be so deeply missed.",
                "My heart goes out to you during this difficult time.",
                "So sorry for your loss. I'm here for you."
            ],
            "meaningful": [
                "A wife is a partner, a confidante, and often the keeper of the family's warmth. Losing her leaves a quiet emptiness in every corner of the home. I'm so sorry, and I'm holding you in my heart.",
                "The love you and your wife shared was a gift — visible in every glance, every shared joke. That love lives on in you and your family. I'm so deeply sorry.",
                "She made a home wherever she was, and her warmth touched everyone who knew her. I'm so sorry for your loss. May her love carry you through.",
                "Some loves define us, and yours with your wife was one of them. I'm so sorry, and I'm here for you."
            ],
            "religious": [
                "May God's peace surround you as you grieve your beloved wife. She rests in His loving arms now. You are in my prayers.",
                "I'm so sorry for your loss. May the Lord be your strength and your refuge in these days. Praying for you and your family.",
                "Praying that your wife rests in eternal peace and that you find comfort in God's presence. You are not alone."
            ]
        },
        "advice": "Acknowledge her warmth and her role in the family. Share a memory of her if you have one. Because men often grieve more privately and rarely ask for help, offer specific practical support: 'I'll bring dinner Thursday' or 'I can take the kids Saturday.' Keep checking in — the second month is often the hardest.",
        "avoid": "Avoid 'be strong for your children' — it pressures him to hide grief. Avoid 'you'll meet someone again someday.' Never ask how she died. Don't say 'she's in a better place' unless you know his beliefs."
    },
    "friend": {
        "label": "Loss of a Friend",
        "intro": "Losing a friend is losing a piece of your own story. Friendships are chosen family, and their loss deserves recognition. When writing to someone who lost a friend, acknowledge the friendship itself — it validates their grief.",
        "messages": {
            "warm": [
                "I am so deeply sorry for the loss of your friend. Friends like that don't come along often, and I know how much they meant to you.",
                "Your friendship was something special — I could see it in how you talked about each other. I'm so sorry for your loss.",
                "Losing a friend is losing a part of your story. I'm thinking of you and holding space for your grief.",
                "I was so saddened to hear about your friend. The memories you shared will stay with you forever. I'm here for you."
            ],
            "short": [
                "I'm so sorry about your friend. They were truly special.",
                "Thinking of you. Losing a friend is so hard.",
                "My heart is with you during this difficult time.",
                "So sorry for your loss. I'm here if you need me."
            ],
            "meaningful": [
                "Friends are the family we choose, and losing one is losing a witness to your life — someone who knew your story and loved you through it. I'm so sorry for your loss.",
                "The greatest tribute to a friend is the way they live on in you — in the jokes you still tell, the places that still hold their memory. I'm so sorry.",
                "Grief for a friend can feel uniquely lonely — the world may not always see how deep it goes. I see it, and I'm holding it with you. I'm so sorry.",
                "Some friendships are soul-deep, and yours was one of them. I'm so sorry, and I'm here for you."
            ],
            "religious": [
                "May God comfort you as you grieve your dear friend. They are at peace in His care. You are in my prayers.",
                "I'm so sorry for your loss. May you find comfort in the promise of eternal life and in the memories you shared.",
                "Praying for peace and strength for you as you mourn your friend. You are not alone."
            ]
        },
        "advice": "Acknowledge the friendship — society often under-recognizes grief for friends, so explicitly validating it matters. Share a memory of them together if you can. Offer to listen or spend time together; grief for a friend can be isolating. Check in on anniversaries and milestones.",
        "avoid": "Avoid 'at least they had a good life' or 'you'll make new friends' — both minimize the loss. Don't compare to other losses. Avoid 'it's been [X] months, how are you still...' — grief has no timeline."
    },
    "coworker": {
        "label": "Loss of a Coworker",
        "intro": "Losing a coworker is losing a familiar face, a teammate, a part of your daily rhythm. Workplace grief is real, even when the relationship was professional. When writing, acknowledge their contribution and the space they filled in the team.",
        "messages": {
            "warm": [
                "I was so sorry to hear about [name]. They were such a valued part of our team, and I know how much you'll miss working alongside them.",
                "Thinking of you during this difficult time. [Name] brought so much to our workplace, and their absence is felt by all of us.",
                "I'm so sorry for the loss of your colleague. They were a wonderful person to work with, and they will be deeply missed.",
                "Sending my condolences. [Name] was someone I always enjoyed working with, and I know they meant a lot to you."
            ],
            "short": [
                "I'm so sorry to hear about your colleague.",
                "Thinking of you and your team during this difficult time.",
                "So sorry for your loss. They will be missed.",
                "My condolences to you and your team."
            ],
            "meaningful": [
                "We spend more waking hours with our colleagues than with anyone else, so losing one leaves a real absence in our days. I'm so sorry, and I'm thinking of your whole team.",
                "A good colleague is someone you trust with the daily rhythm of work — and losing that trust and familiarity is a genuine loss. I'm so sorry.",
                "The workplace will feel different without them, and it's okay to grieve that. I'm holding your team in my thoughts. I'm so sorry."
            ],
            "religious": [
                "May God grant your colleague eternal rest and bring peace to you and your team. You are in my prayers.",
                "I'm sorry for your loss. May you find comfort in your faith during this difficult time.",
                "Praying for strength and peace for you and your colleagues as you mourn together."
            ]
        },
        "advice": "Workplace grief is often under-acknowledged — a sincere message matters more than you think. Mention their contribution, their humor, or the daily presence you'll miss. Offer practical support at work: cover a shift, take over a meeting. Grief in the workplace can be awkward; your acknowledgment makes it a little easier.",
        "avoid": "Avoid 'at least you didn't work with them that long' or treating it as minor. Don't say 'the show must go on' — work will resume, but grief doesn't follow a schedule. Never ask for details of the death."
    },
    "grandmother": {
        "label": "Loss of Grandmother",
        "intro": "Grandmothers hold a special place — the keeper of family stories, the source of unconditional warmth. Losing one is losing a piece of family history. When writing, acknowledge her role in the family and the legacy she leaves.",
        "messages": {
            "warm": [
                "I am so deeply sorry for the loss of your grandmother. She was the heart of your family, and her warmth will be so deeply missed.",
                "Your grandmother was so special — I remember how her eyes lit up when she talked about you. I'm so sorry for your loss.",
                "Grandmothers are the keepers of our family stories, and losing yours is losing a living piece of history. I'm thinking of you and your family.",
                "I was so saddened to hear about your grandma. The love she gave your family will live on in all of you. I'm so sorry."
            ],
            "short": [
                "I'm so sorry about your grandmother. She was so loved.",
                "Thinking of you and your family. She will be deeply missed.",
                "My heart goes out to you. Grandmothers are irreplaceable.",
                "So sorry for your loss. She was a wonderful woman."
            ],
            "meaningful": [
                "Grandmothers are the roots of our family trees — the ones who remember where we came from and love us unconditionally. Losing yours is losing a living link to your family's story. I'm so sorry.",
                "The recipes, the stories, the way she made you feel — those are her legacy, and they live on in you. I'm so sorry for your loss.",
                "A grandmother's love is one of the most unconditional loves we ever know. Losing that is profound. I'm holding you in my heart.",
                "She poured her love into your family for a lifetime, and that love doesn't end — it lives in every story you'll tell about her. I'm so deeply sorry."
            ],
            "religious": [
                "May God's peace surround you as you grieve your precious grandmother. She is at rest in His loving arms. You are in my prayers.",
                "I'm so sorry for your loss. May you find comfort knowing she is at peace with God and watching over your family.",
                "Praying for your family as you honor your grandmother's life and legacy. She is safe in the Lord's care."
            ]
        },
        "advice": "Acknowledge her role as family matriarch and storykeeper. If you have a memory of her — a recipe, a saying, a moment — share it. Grandmother grief often includes grief for the family bonds she held together; acknowledge that. Offer to help with family arrangements or gatherings.",
        "avoid": "Avoid 'she lived a long life' as a way to minimize the loss — even a long life leaves a big hole. Don't say 'she's watching over you' unless you know their beliefs. Avoid making the message about your own grandmother unless it's relevant and welcomed."
    },
    "grandfather": {
        "label": "Loss of Grandfather",
        "intro": "Grandfathers are often the quiet pillars of a family — storytellers, mentors, the steady presence at every holiday. Losing one is losing wisdom and history. When writing, acknowledge his legacy and the lessons he passed on.",
        "messages": {
            "warm": [
                "I am so deeply sorry for the loss of your grandfather. He was a pillar of your family, and his wisdom will be so deeply missed.",
                "Your grandfather was such a kind and steady presence — I know how much he meant to you. I'm thinking of you and your family.",
                "I was so saddened to hear about your grandpa. The stories and lessons he shared are a gift that will live on through you. I'm so sorry.",
                "Grandfathers leave footprints on our hearts. Yours certainly did. I'm so sorry for your loss."
            ],
            "short": [
                "I'm so sorry about your grandfather. He was a wonderful man.",
                "Thinking of you and your family. He will be deeply missed.",
                "My heart goes out to you during this difficult time.",
                "So sorry for your loss. He was truly respected and loved."
            ],
            "meaningful": [
                "Grandfathers are the storytellers and the quiet mentors — the ones who taught us patience, hard work, and how to laugh. Your grandfather gave you those gifts, and they live on in you. I'm so sorry.",
                "The handshake, the stories, the way he always knew what to say — those moments are his legacy, carried forward by everyone he touched. I'm so deeply sorry.",
                "A grandfather's love is steady and enduring, like the roots of an old tree. Losing yours is losing shade and shelter. I'm holding you in my heart.",
                "He built a legacy not just in what he did, but in who he raised. I'm so sorry for your loss."
            ],
            "religious": [
                "May God grant your grandfather eternal rest and bring your family His peace. You are in my prayers.",
                "I'm so sorry for your loss. May you find comfort in the promise of eternal life and in the legacy he left behind.",
                "Praying for your family as you honor your grandfather's life. He is at peace with the Lord."
            ]
        },
        "advice": "Acknowledge his legacy — the stories, the lessons, the family he built. Share a specific memory if you have one. Grandfather grief often connects to family identity; acknowledge his role in shaping yours. Offer help with arrangements or simply be present.",
        "avoid": "Avoid 'he lived a full life' as dismissal. Don't say 'be strong for grandma' — everyone grieves differently. Avoid 'he's in a better place' unless you know their beliefs. Don't ask about inheritance or practical matters."
    },
    "pet": {
        "label": "Loss of a Pet",
        "intro": "Losing a pet is losing a family member — a constant companion, a source of unconditional love. Pet grief is real and deserves genuine acknowledgment. When writing, treat the loss with the same respect as any other.",
        "messages": {
            "warm": [
                "I am so deeply sorry for the loss of your beloved [pet]. They were such a wonderful companion, and I know how much joy they brought you.",
                "Losing a pet is losing a family member. I'm so sorry, and I'm thinking of you during this difficult time.",
                "Your [pet] was so lucky to have you — the love you gave them was evident in every moment. I'm so sorry for your loss.",
                "They may have been with you for a part of your life, but you were their whole life. I'm so sorry, and I'm holding you in my heart."
            ],
            "short": [
                "I'm so sorry about your [pet]. They were so loved.",
                "Thinking of you. Losing a pet is so hard.",
                "My heart goes out to you. Pets are family.",
                "So sorry for your loss. They were a special companion."
            ],
            "meaningful": [
                "Pets ask for nothing but love and give everything back. Your [pet] gave you years of that unconditional love, and losing them leaves a real emptiness. I'm so sorry.",
                "The house feels different, the routine feels different, and the silence where they used to be is loud. That's how much they mattered. I'm so sorry for your loss.",
                "They were a constant — through good days and hard days, they were there. That kind of presence leaves a hole nothing else fills. I'm so deeply sorry.",
                "Grief for a pet is often underestimated by others, but it's a profound loss. I see it, and I'm holding it with you."
            ],
            "religious": [
                "May you find comfort in the love you shared with your beloved pet. They are at peace now, and you are in my prayers.",
                "I'm so sorry for your loss. May the memories of your [pet] bring you comfort, and may you feel peace in your grief.",
                "Praying for your heart as you mourn your dear companion. The love you shared was a gift."
            ]
        },
        "advice": "Treat pet loss with genuine respect — never minimize it. Say the pet's name and acknowledge the specific joy they brought. Offer concrete support: a walk, a meal, or simply being present. Many people grieve pets as deeply as people; your acknowledgment is a gift. Check in a few weeks later — pet grief can hit hardest after the initial shock fades.",
        "avoid": "Avoid 'it was just a pet' — this is deeply hurtful. Avoid 'you can always get another one' — never suggest replacement. Don't rush them to 'get over it.' Avoid 'at least they didn't suffer' unless you know the circumstances."
    }
}

# 合并进 wordbank.json
with open(f'{BASE}/wordbank.json', encoding='utf-8') as f:
    wb = json.load(f)

for key, data in NEW_RELATIONSHIPS.items():
    wb[key] = data
    print(f'✅ 新增关系: {key} ({data["label"]})')

wb['meta']['version'] = '0.2'
wb['meta']['note'] = wb['meta']['note'].replace('v0.1', 'v0.2').replace('三套', '十套')

with open(f'{BASE}/wordbank.json', 'w', encoding='utf-8') as f:
    json.dump(wb, f, ensure_ascii=False, indent=2)

# 统计
total_msgs = sum(len(rel['messages'].get(t, [])) for rel in wb.values() if isinstance(rel, dict) and 'messages' in rel for t in ['warm','short','meaningful','religious'])
print(f'\n🎉 词库 v0.2 完成：{len([k for k in wb if isinstance(wb[k], dict) and "messages" in wb[k]])} 个关系集，共 {total_msgs} 条消息')
