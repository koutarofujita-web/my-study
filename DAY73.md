# ⚡ SIEMログ分析ツール：リアルタイム・ストリーム相関分析エンジンの実装 (Day 2)

SIEMシステムの核心部である**「リアルタイム・ストリーム相関分析エンジン」**をPythonおよびRedisを用いて独自実装しました。
単一のログ判定にとどまらず、**「複数のイベントが時系列でどのように発生したか（シーケンス）」** をリアルタイムで分析・検知するロジックを構築しています。

---

## 🎯 課題と解決したアプローチ

### 課題：遅延ログ（Out-of-order）問題と状態保持
ネットワーク遅延等により、ログが発生順（イベント時間）通りに届かない場合、単純な到達順処理では正しい攻撃シーケンスを検知できません。
また、時間軸を跨ぐセッション状態のリアルタイム保持が必要です。

### 解決策：Redis Sorted Set を活用したタイムウィンドウ処理
* **イベント時間ベースの自動ソート**: 
  ログ受信時、Redisの **Sorted Set (ZSET)** に `Score = イベント発生時刻 (Unix Epoch)` として保存。遅れて届いたログもメモリ内で自動的に正しい時系列順に整列されます。
* **メモリ効率とスライドウィンドウ**:
  `ZREMRANGEBYSCORE` を使用し、指定したタイムウィンドウ（例: 過去5分間）より古いデータを自動削除。メモリリークを防ぎつつ常に直近の文脈を維持します。

---

## 💡 検知ロジック（ステートマシン構成）

以下の複合攻撃シーケンスをリアルタイムに追跡・判定しています。

1. **Phase 1 (BruteForce Attempt)**: 5分以内に同一IPから `LOGIN_FAILED` が5回以上発生
2. **Phase 2 (Breach)**: Phase 1の後に `LOGIN_SUCCESS` が発生（アカウント乗っ取り）
3. **Phase 3 (Data Exfiltration)**: ログイン成功後に `/admin/db_dump.sql` 等の機密ファイルへアクセス
   👉 **上記シーケンスが揃った瞬間に `CRITICAL ALERT` を発報**

---

## 🛠️ 核心実装（Pythonコード抜粋）

```python
def process_log(log_event):
    ip = log_event["ip"]
    event_time = log_event["timestamp"]
    timeline_key = f"timeline:{ip}"

    # 1. Sorted Setへ追加 (Score = 発生時刻) -> 遅延ログも自動整列
    r.zadd(timeline_key, {json.dumps(log_event): event_time})

    # 2. 過去5分より古いログを削除（スライドウィンドウ＆メモリ対策）
    cutoff_time = event_time - WINDOW_SECONDS
    r.zremrangebyscore(timeline_key, "-inf", cutoff_time)

    # 3. 時系列順に整列されたログを取得して相関チェック
    raw_logs = r.zrange(timeline_key, 0, -1)
    logs = [json.loads(l) for l in raw_logs]
    detect_sequence_attack(ip, logs)
