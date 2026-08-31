## アレンジしてオリジナル問題を作成
あなたはカフェの店長です。お店で一番人気の特製スムージーを n 杯作ることになりました。
このスムージーを 1 杯作るためには、新鮮なイチゴが 1.5 kg 必要です。
スムージーを n 杯作るために必要なイチゴの合計量（kg）を計算して出力するプログラムを作成してください。
## 入力値
n
## 入力をされる値
ｎ
## 期待される出力
必要なイチゴの合計量を小数点以下を含む数値で 1 行に出力してください。末尾に改行を入れてください。
## 解答例
import sys

def main():
    # 標準入力から全体の文字列を取得して数値に変換
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    
    # 1杯あたり1.5kg必要なため、n杯分を計算
    total_strawberries = n * 1.5
    
    # 結果を出力
    print(total_strawberries)

if __name__ == "__main__":
    main()
