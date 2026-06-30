

## アレンジ問題
ある日、上司から奇妙な指令が下った。
「ターゲットのファイルサーバー（コードネーム：JON-PC）に、物理的な負荷テストを行う。
用意した超重量級のデータボムの総重量を瞬時に算出するスクリプトを構築せよ」と。

我々セキュリティチームは、機密保持（NDA）に抵触しないよう仕様をカモフラージュし、
以下の計算プログラムを開発した。

## 📋 （仕様）
組織のインフラがボムの総重量に耐えられるか検証するため、
以下の入力から総重量を求めて標準出力する。

### 入力されるデータ
1. 最初に、投下予定のボムの総数 `bomb_count` が入力される。
2. 次に、ボム1個あたりの凶悪な重量 `single_bomb_weight` が入力される。

### 出力
* 算出した総重量（ `bomb_count` × `single_bomb_weight` ）

---

## 💻 実装コード 
```csharp
using System;

class Program
{
    static void Main()
    {
        // 1行目：ボムの総数を取得
        int bombCount = int.Parse(Console.ReadLine());
        
        // 2行目：ボム1個あたりの重量を取得
        int singleBombWeight = int.Parse(Console.ReadLine());
        
        // 総重量の計算
        int totalWeight = bombCount * singleBombWeight;
        
        // 結果を標準出力
        Console.WriteLine(totalWeight);
    }
}
