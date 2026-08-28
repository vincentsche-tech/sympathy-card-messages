#!/usr/bin/env python3
"""
sympathy 站关系页脚手架：
1. 给所有 17 个关系/主题页（除主页 + what-to-write + about/contact/privacy/terms）底部追加
   "More Condolence Messages by Relationship" 网格，互相链接 8 个其他关系页
2. 给 index.html 底部追加 "Browse by Relationship" 网格，列 12 个关系页（首页 Direct 流量
   主入口，加这区块能把用户分流到关系页，让谷歌爬到孤儿关系页）

幂等：通过 h2 字符串 "More Condolence Messages by Relationship" 检测已插入
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).parent.parent

# ============ 18 个关系/主题页映射（filename -> (Display title, Description)）============
PAGE_META = {
    'bible-verses-for-loss-of-mother.html': ('Bible Verses for Loss of Mother', 'Scripture for a mom\u2019s passing.'),
    'condolence-messages-for-loss-of-brother.html': ('Loss of Brother', 'Words for losing a brother.'),
    'condolence-messages-for-loss-of-coworker.html': ('Loss of Coworker', 'Messages for a colleague\u2019s loss.'),
    'condolence-messages-for-loss-of-daughter.html': ('Loss of Daughter', 'Words for losing a daughter.'),
    'condolence-messages-for-loss-of-father.html': ('Loss of Father', 'Words for losing a dad.'),
    'condolence-messages-for-loss-of-friend.html': ('Loss of Friend', 'Messages when a friend passes.'),
    'condolence-messages-for-loss-of-grandfather.html': ('Loss of Grandfather', 'Words for a grandpa\u2019s passing.'),
    'condolence-messages-for-loss-of-grandmother.html': ('Loss of Grandmother', 'Words for a grandma\u2019s passing.'),
    'condolence-messages-for-loss-of-husband.html': ('Loss of Husband', 'Words for a husband\u2019s passing.'),
    'condolence-messages-for-loss-of-mother.html': ('Loss of Mother', 'Messages that honor a mom\u2019s love.'),
    'condolence-messages-for-loss-of-pet.html': ('Loss of Pet', 'Words for a beloved companion.'),
    'condolence-messages-for-loss-of-sister.html': ('Loss of Sister', 'Words for losing a sister.'),
    'condolence-messages-for-loss-of-son.html': ('Loss of Son', 'Words for losing a son.'),
    'condolence-messages-for-loss-of-wife.html': ('Loss of Wife', 'Words for a wife\u2019s passing.'),
    'meaningful-condolence-messages.html': ('Meaningful Messages', 'Deeper, heartfelt messages.'),
    'religious-condolence-messages.html': ('Religious Messages', 'Faith-based and spiritual sympathy.'),
    'short-condolence-messages.html': ('Short Messages', 'Brief and meaningful, for texts.'),
    'simple-condolence-messages.html': ('Simple Messages', 'Plain-language, sincere words.'),
}

GRID_NEEDED = list(PAGE_META.keys())

# ============ Grid block template =============
def make_grid_block(title, links):
    """Build a .card with a grid of scene-cards. links = list of (href, label, desc)."""
    items = ''.join(
        f'\n      <a class="scene-card" href="{href}"><b>{label}</b><span>{desc}</span></a>'
        for href, label, desc in links
    )
    return f'''
  <div class="card">
    <h2>{title}</h2>
    <div class="grid">{items}
    </div>
  </div>
'''


def make_relationship_grid(self_fn, count=8):
    """Build a 'More Condolence Messages by Relationship' grid: 8 random-but-deterministic siblings."""
    others = sorted([fn for fn in GRID_NEEDED if fn != self_fn])
    # 取前 8 个（按文件名字典序，避开自己即可）
    picks = others[:count]
    links = [('/' + fn, *PAGE_META[fn]) for fn in picks]
    return make_grid_block('More Condolence Messages by Relationship', links)


def make_homepage_grid():
    """首页 'Browse by Relationship' 网格：列 12 个最常搜的关系页。"""
    picks = [
        'condolence-messages-for-loss-of-mother.html',
        'condolence-messages-for-loss-of-father.html',
        'condolence-messages-for-loss-of-grandmother.html',
        'condolence-messages-for-loss-of-grandfather.html',
        'condolence-messages-for-loss-of-husband.html',
        'condolence-messages-for-loss-of-wife.html',
        'condolence-messages-for-loss-of-son.html',
        'condolence-messages-for-loss-of-daughter.html',
        'condolence-messages-for-loss-of-brother.html',
        'condolence-messages-for-loss-of-sister.html',
        'condolence-messages-for-loss-of-friend.html',
        'condolence-messages-for-loss-of-coworker.html',
    ]
    links = [('/' + fn, *PAGE_META[fn]) for fn in picks]
    return make_grid_block('Browse by Relationship', links)


# ============ Insertion helpers =============
def insert_relationship_grid(c, block):
    """在 'More ...' 网格卡片整体结束处（即 grid</div></div>）之后、下一卡片开始前
    追加新网格卡。任何 H2 文字的 More 都匹配。
    """
    # 找"任意 More 开头 H2 + grid 卡"的"卡级"</div></div> 收尾
    # 写法：先用一次正则找 More 开头的 h2，再找紧跟的 .grid ... </div> 块，再找匹配的 </div>
    # pattern: <h2>More ...</h2>\s*<div class="grid">...</div>\s*</div>
    pattern = r'(<h2>More [^<]*</h2>\s*<div class="grid">.*?</div>\s*\n)\s*(</div>)'
    m = re.search(pattern, c, flags=re.S)
    if not m:
        # fallback: 在 </main> 之前插入
        m2 = re.search(r'(\n</main>)', c)
        if not m2:
            return c, False
        return c[:m2.start()] + block.rstrip() + c[m2.start():], True
    # 在"卡的 closing div"前注入（这样新卡 跟在 旧卡的 closing 前）
    insert_pos = m.start(2)
    return c[:insert_pos] + block.rstrip() + '\n  ' + c[insert_pos:], True


def insert_homepage_grid(c, block):
    """在首页底部、FAQ 卡之前插入新网格。先看首页有无现成 footer-like 结构"""
    # 首页 vs 子页结构可能不同，先 head + main 看一下 hero 后是否有 grid
    # 简单策略：在 </main> 前插入
    pattern = r'(\n</main>)'
    m = re.search(pattern, c)
    if not m:
        return c, False
    return c[:m.start()] + block.rstrip() + c[m.start():], True


def is_idempotent_rel(c):
    return 'More Condolence Messages by Relationship' in c


def is_idempotent_home(c):
    return 'Browse by Relationship' in c


def main():
    dry = '--dry' in sys.argv
    written = 0
    skipped = 0

    # 1. 关系页（17 个）互相链接
    for fn in GRID_NEEDED:
        fp = ROOT / fn
        if not fp.exists():
            print(f'SKIP {fn} (not found)')
            skipped += 1
            continue
        c = fp.read_text(encoding='utf-8')
        if is_idempotent_rel(c):
            print(f'{fn}: ALREADY-REL-GRID (skip)')
            skipped += 1
            continue
        block = make_relationship_grid(fn)
        new_c, ok = insert_relationship_grid(c, block)
        if not ok:
            print(f'{fn}: INSERT-FAILED (skip)')
            skipped += 1
            continue
        print(f'{fn}: rel-grid added')
        if not dry:
            fp.write_text(new_c, encoding='utf-8')
            written += 1

    # 2. 首页 "Browse by Relationship"
    home = ROOT / 'index.html'
    if home.exists():
        c = home.read_text(encoding='utf-8')
        if is_idempotent_home(c):
            print(f'index.html: ALREADY-HOME-GRID (skip)')
        else:
            block = make_homepage_grid()
            new_c, ok = insert_homepage_grid(c, block)
            if ok:
                print(f'index.html: homepage-grid added')
                if not dry:
                    home.write_text(new_c, encoding='utf-8')
                    written += 1
            else:
                print(f'index.html: INSERT-FAILED (skip)')

    print(f'\nDone. Written={written} Skipped={skipped}  ({"DRY" if dry else "WROTE"})')


if __name__ == '__main__':
    main()
