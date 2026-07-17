# アレンジしてオリジナル問題を作成

## 問題
A君は砂漠の惑星に不時着してしまいました。
この惑星では「水」が通貨の代わりです。
A君はもともと X ml の水を所持していました。
しかし、昨日はオアシスを発見したため Y ml の水を手に入れることができました。
気が緩んだ今日、凶暴な砂漠のトカゲに襲われてしまい、背中の水筒に穴が空いて Z ml の水を失ってしまいました。
A君の現在の水の所持量は何mlですか？

## 入力例
180
150
50
## 出力例
280


### 回答code例
import sys




    # 入力が足りない場合のガード
    if len(input_data) < 3:
        return

    # 世界観に合わせた変数名で入力を受け取る
    initial_water = int(input_data[0])  # もともと所持していた水 (X)
    gained_water = int(input_data[1])  # オアシスで手に入れた水 (Y)
    lost_water = int(input_data[2])  # トカゲに襲われて失った水 (Z)

    # 現在の水の所持量を計算
    current_water = initial_water + gained_water - lost_water

    # 結果を出力
    print(current_water)


if __name__ == "__main__":
    main()
