## アレンジしてオリジナル問題を作成

### 問題文
あなたは給料日前日です。 
今夜を生き延びるためのお弁当を求めて、閉店間際のスーパーに滑り込みました。
疲れ切ったあなたの前に、2つの選択肢が立ちはだかります。
割引はないが、最初から良心的な価格設定の「塩むすびセット」（定価 400円） 半額シールを期待したが
無情にも「30%OFF」のシールで踏みとどまっている「豪華幕の内弁当」（定価 500 円）
あなたの財布の残高をできるだけ来月に残すために、より安い方を購入したときの金額を出力してください。 
なお、レジの古いシステムは1円未満の計算に対応していないため、30%OFFの計算で生じた小数点以下は無条件で切り捨てられますあなたの所持金は X 円です。

### 解答コード
```python
X = 380
price_shio = 400
price_makunouchi = int(500 * 0.7)
if X < price_shio and X < price_makunouchi:
    print(-1)
elif X >= price_shio and X >= price_makunouchi:
    print(min(price_shio, price_makunouchi))
elif X >= price_shio:
    print(price_shio)
else:
    print(price_makunouchi)
