# アレンジしてオリジナル問題を作成
あなたはIoT温度・湿度センサーのシステム開発を担当しています。
朝（a）、昼（b）、夜（c）の3回の 「気温（℃）」 と 「湿度（%）」 が記録されたログデータから、本日のシステムステータスを判定して出力するプログラムを作成してください。

ステータスは以下の 優先度ルール（上にあるルールが優先）に従って決定されます。

DANGER（熱中症警戒警報）:
最高気温が 35℃以上、かつその時の湿度が 60%以上 の時間帯が1回以上存在する場合。

WARNING（寒冷または乾燥注意）:
最低気温が 10℃未満、または最低湿度が 30%未満 の場合。

OK（正常）:
上記の条件のいずれにも当てはまらない場合。

さらに、判定結果の次の行に、本日の 「最高気温」 と 「最低気温」 を 最高/最低（例: 33/21）の形式で出力してください。

## 入力される値
a_temp a_hum
b_temp b_hum
c_temp c_hum

## 入力例１
23 50
36 65
21 40

## 出力例１
DANGER
36/21

## 解答コード
def check_climate_status():
    # 1. 朝・昼・夜の気温と湿度をそれぞれ取得（1行に2つの数値）
    a_temp, a_hum = map(int, input().split())
    b_temp, b_hum = map(int, input().split())
    c_temp, c_hum = map(int, input().split())

    # 2. 最高気温・最低気温の算出
    max_temp = max(a_temp, b_temp, c_temp)
    min_temp = min(a_temp, b_temp, c_temp)
    
    # 最低湿度の算出
    min_hum = min(a_hum, b_hum, c_hum)

    # 3. 条件判定
    # 条件1: 危険状態（気温35以上 かつ 湿度60以上 の時間帯があるか）
    is_danger_a = (a_temp >= 35 and a_hum >= 60)
    is_danger_b = (b_temp >= 35 and b_hum >= 60)
    is_danger_c = (c_temp >= 35 and c_hum >= 60)

    if is_danger_a or is_danger_b or is_danger_c:
        status = "DANGER"
    # 条件2: 警告状態（最低気温10未満 または 最低湿度30未満）
    elif min_temp < 10 or min_hum < 30:
        status = "WARNING"
    # 条件3: 正常
    else:
        status = "OK"

    # 4. 結果の出力
    print(status)
    print(f"{max_temp}/{min_temp}")

if __name__ == '__main__':
    check_climate_status()
