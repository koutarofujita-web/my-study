# アレンジ問題を作成

## 問題
我々の開発チームに所属するAが、プロダクション環境で2つの強力な呪文を融合させる新魔法の開発に取り組んでいます。
しかし、彼の脳内IDEでは完璧に動いていたものの、現実の世界での実装方法が分からず、「クックック…闇の力が足りない…」と呟いています。
Aの代わりに、2つの呪文を結合して新しい最強の呪文を出力するスクリプトを書いてあげてください。

import sys

def fuse_magic_spells():
    """
   
    lines = sys.stdin.read().splitlines()
    
    if len(lines) < 2:
        print
        return

    spell_b = lines[0]
    spell_c = lines[1]
    
    # 禁忌の錬金術：+ 演算子による文字結合
    forbidden_new_spell = spell_b + spell_c
    
    # 爆誕した新呪文を世界に解き放つ
    print(forbidden_new_spell)

if __name__ == "__main__":
    fuse_magic_spells()
