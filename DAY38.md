 ## オリジナル問題を作成。

 ### 問題
ポテトチップスの袋の高さ a (cm) と、
実際に中に入っているポテトチップスが積み上がっている高さ b (cm) が与えられます。
開けた瞬間に誰もが絶望する「あの空気の隙間（空間）」の広さを求めてください。
なお、悲しいことに、袋の高さが中身の高さ未満になることは絶対にありません。

### 入力される値
a b

### 出力される値
空間の高さ（差分）

### code

python3

import sys

def main():
    # 標準入力から a と b を取得（スペース区切り）
    input_line = sys.stdin.read().split()
    
    if not input_line:
        return

    # 文字列を整数に変換
    a = int(input_line[0])  # 袋の高さ (cm)
    b = int(input_line[1])  # 中身のポテトチップスの高さ (cm)

    # 絶望の空間（差分）を計算
    despair_gap = a - b

    # 結果を出力
    print(despair_gap)

if __name__ == '__main__':
    main()
