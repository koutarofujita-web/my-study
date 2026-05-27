## アレンジしてオリジナル問題を作成。

### 問題文
A君は10ページある宿題の5割を、友人のB君に代わりにやってもらいました。しかし、それが先生にバレてしまい、
バツとしてとして「B君にやってもらった分の10倍のページ数」の宿題を翌週に自分でやるよう命じられました。
A君が「最初の週に自分でやったページ数」と「翌週にペナルティとしてやったページ数」の合計は、最終的に何ページになるか出力してください。

### 解答コード
```python3

total_pages = 10
first_week_done = total_pages * 0.5
b_friend_done = total_pages - first_week_done
penalty_pages = b_friend_done * 10
answer = first_week_done + penalty_pages
print(int(answer))

## 出力結果
```text
55
