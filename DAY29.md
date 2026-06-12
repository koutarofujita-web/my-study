## アレンジしてオリジナル問題を作成。

### 問題文
あなたは、世界で最も熱いサウナ「熱風地獄・千葉の湯」の見習い熱波師です。
ここには、毎日3人の「自称・我慢の限界を知らない猛者たち」がやってきます。
師匠から課されたあなたの任務は一つ。「本日、最もサウナ室の温度を爆上げした
『最高に熱い漢（最高気温）』が誰だったかを特定し、電光掲示板に叩き込むこと」です。
本日も3人の猛者が、それぞれの限界温度（$t_1, t_2, t_3$）を残して、水風呂へと去っていきました。
さあ、最高温度を弾き出すシステムを起動するのです！
### 入力、出力
入力される値3行にわたり、猛者たちがサウナ室を限界まで追い込んだ温度（整数）が与えられます。

3人の中で最も高かった温度（最高気温）のみを、1行で出力してください。

### 解答コード
```python3
using System;
using System.Linq;

class Program
{
    static void Main()
    {
        
        int t1 = int.Parse(Console.ReadLine());
        int t2 = int.Parse(Console.ReadLine());
        int t3 = int.Parse(Console.ReadLine());

        
        int maxTemperature = Math.Max(t1, Math.Max(t2, t3));

        
        Console.WriteLine(maxTemperature);
    }
}
