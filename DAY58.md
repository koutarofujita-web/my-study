# アレンジしてオリジナル問題を作成
## 問題
あなたは深夜のデバッグ作業中、ふと気がつくと不気味な異世界「ヌル・ポインタ」に迷い込んでしまいました。
背後からは、メモリを食い荒らす巨大なバグの怪物「セグメンテーション・フォールト」が恐ろしい雄叫びを上げて迫ってきています！

手元にあるのは、ゴミ捨て場から拾い集めたガラクタで急造した**「手動式レール台車」**のみ。
この異世界から脱出する安全圏（ゲート）までの距離は $D\text{ km}$ です。

この台車を動かすには、特殊な魔力結晶「エーテル・バッテリー」を消費する必要があります。消費エネルギーの仕様は以下の通りです。

* 走行距離が $3\text{ km}$ 以下（初動フェーズ）の場合、台車の起動と加速に一律 **$500\text{ ml}$** の魔力を消費します。
* 走行距離が $3\text{ km}$ を超えた場合、超えた分の距離に対して **$1\text{ km}$ あたり $K\text{ ml}$** の魔力が追加で加算されます。

無事に脱出ゲートにたどり着くために必要な、エーテル・バッテリーの総消費量（エネルギー）を計算するプログラムを作成してください。

---

## 入力される値
```text
D K


```python
import sys
import math

def calculate_required_energy():
    
    input_line = sys.stdin.readline().split()
    if not input_line:
        return
    
    D = float(input_line[0])
    K = int(input_line[1])
    
   
    initial_energy = 500  
    safe_distance_limit = 3.0  
    
    
    if D <= safe_distance_limit:
       
        total_energy = initial_energy
    else:
      
        extra_distance = D - safe_distance_limit
        extra_energy = extra_distance * K
        total_energy = initial_energy + extra_energy
        
   
    print(math.floor(total_energy))

if __name__ == '__main__':
    calculate_required_energy()
