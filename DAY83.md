## アレンジをしてオリジナル問題を作成
システム監視ツールを作成しています。現在のメモリ使用量 $N$ (MB) が標準入力から与えられます。
安全基準値は 1000 MB です。メモリ使用量 ALERT が基準値 1000 MB 以上 であれば警告を出力するために
ALERT を、基準値未満（1000 MB より小さい）であれば OK を出力するプログラムを作成してください。

## 入力予想値
N

## 出力予想値
基準値以上なら ALERT、
未満なら OK を 1 行で出力してください。
末尾には改行を入れてください。


### 解答コード例
import sys


def check_resource_threshold():
    # 標準入力から使用量を取得
    usage = int(sys.stdin.read().strip())

    # 閾値1000MB以上かどうかを判定
    if usage >= 1000:
        print("ALERT")
    else:
        print("OK")


if __name__ == "__main__":
    check_resource_threshold()
