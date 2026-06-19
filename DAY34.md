 ## オリジナル問題を作成。

### 問題文

あなたは魔界のコンビニ「ダーク・マーチャント」の新人アルバイト店員です。本日のお客さまは、なんと大魔王様。
大魔王様は極めて気が短く、お釣りの計算を1ミリ秒でも、あるいは1魔貨でも間違えようものなら、世界はたちまち闇に包まれます。

大魔王様が購入された商品の合計魔力（金額）$n$ と、支払われた魔貨（支払額）$m$ が与えられます。
大魔王様に無事にお返しすべきお釣りの魔力を正確に計算し、世界の平和を守ってください。

---

##  Input Specification (入力仕様)



```text
n
m


```python
import sys


def calculate_demon_change():
   
    try:
       
        input_data = sys.stdin.read().split()

        if len(input_data) < 2:
            return

       
        total_magical_cost = int(input_data[0])  
        dark_lord_payment = int(input_data[1])  

        
        change_to_return = dark_lord_payment - total_magical_cost

        
        if change_to_return < 0:
            
            print(0)
        else:
            
            print(change_to_return)

    except Exception as e:
        
        print(0)


if __name__ == "__main__":
    calculate_demon_change()
