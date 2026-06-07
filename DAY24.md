## アレンジしてオリジナル問題を作成。

### 問題文
人類の未来をかけた宇宙移民船が、新たな惑星に向けて航行しています。
この船には $N$ 人 の乗組員が乗っていますが、目的地に到着するまでの間、コールドスリープ（人工冬眠）カプセルに入らなければなりません。
宇宙船に搭載されている最新型スリープポッドは、1基につきぴったり $M$ 人 を同時に収容できる巨大なグループカプセルです。
安全基準により、ポッドの定員（$M$ 人）が完全に埋まらないと、そのポッドは起動できない仕様になっています。
乗組員を次々とポッドに詰め込んでいった結果、最後にどうしても $M$ 人に満たず、カプセルに入れ漏れてしまった
「宇宙船の治安維持用に見張りとして残される切ないメンバーの数」を求めてください。全員ぴったり収容できた場合は、見張りは不要（0）となります。

### 入力、出力
（ $N \pmod M$ を出力）　　　　

### 解答コード
```python3
import sys


def main():
    """Calculates the number of left-behind crew members (N % M).

    N: Total number of crew members
    M: Capacity of a single sleep pod
    """
    # sys.stdin.read().split() 
    
    input_data = sys.stdin.read().split()

    if not input_data:
        return

   
    N = int(input_data[0])
    M = int(input_data[1])

   
    left_over = N % M

   
    print(left_over)


if __name__ == "__main__":
    main()
