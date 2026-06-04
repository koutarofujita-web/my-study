## アレンジしてオリジナル問題を作成。

### 問題文
魔乗合馬車（マサラバシャ）の料金算出ギルドクエスト
冒険者の街「ヤチヨディア」から出発する魔導馬車は、非常に気性の荒い御者が運営している。
この馬車は、乗るだけで**「御者への賄賂」として100ゴールドが必要だ。
そこからさらに、魔物が徘徊する危険エリア（区間）を1つ突破するごとに、御者のストレス料として10ゴールド**が加算されるシステムになっている。
任務：駆け出しの冒険者 $N$ 人…ではなく、移動した区間数 $N$ が与えられるので、
生きて次の街にたどり着くために必要な総ゴールドを算出する魔導回路（プログラム）を構築せよ。

### 解答コード
```python3

import sys


def calculate_bribe(danger_zones: int) -> int:
    

    Args:
        danger_zones (int): 

    Returns:
        int: 
    """
    
    base_bribe = 100

   
    stress_premium_per_zone = 10

   
    total_gold_required = base_bribe + (danger_zones * stress_premium_per_zone)

    return total_gold_required


if __name__ == "__main__":
    
    try:
       
        input_data = sys.stdin.read().strip()

        if not input_data:
            raise ValueError
        n = int(input_data)

       
        if n < 0:
            print(
                
                file=sys.stderr,
            )
            sys.exit(1)

        
        result_gold = calculate_bribe(n)
        print(result_gold)

    except ValueError:
      
        print(
            
            file=sys.stderr,
        )
        sys.exit(1)
