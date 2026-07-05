# TryHackMe 学習記録: OWASP Juice Shop 攻略への道

## 📌 今日の進捗 
TryHackMeの「OWASP Juice Shop」ルームにおいて、攻撃環境および検証用ターゲットマシンのセットアップを完了し、ユーザー登録までの手順を確認しました。

### 💻 実施内容と環境構築
1. **仮想環境の立ち上げ**
   - TryHackMe上で攻撃用マシン（AttackBox）とターゲットマシン（Juice Shopサーバー）を起動。
2. **Burp Suiteの初期設定**
   - AttackBox内でBurp Suite Community Editionを起動。
   - Linux環境におけるブラウザ起動時の競合を回避するため、`--no-sandbox`（サンドボックス無効化）のチェックを入れてBurpブラウザの立ち上げに成功。
3. **プロキシ経由でのターゲットアクセス**
   - ターゲットマシンのBurpブラウザからアクセス。
   - 初期状態の `Intercept is on` による通信のせき止めを `Intercept is off` に切り替えることで、正常にJuice Shopのショップ画面（All Products）の描画を確認。
4. **ユーザー登録機能の確認**
   - `Account` -> `Login` から `Not yet a customer?` の導線を確認し、
   - テスト用のアカウント作成手順までをキャッチアップ。

### 🔍 遭遇した課題と解決策 (Troubleshooting)
- **課題**: Burpブラウザ起動時にサンドボックス関連のエラー（Burp Browser Error）が発生。
- **解決策**: `Proxy settings` > `Burp's browser` 内の `Allow Burp's browser to run without a sandbox` にチェックを入れることで解決。
- **課題**: Intercept機能が有効なままになっており、ブラウザが読み込み中の状態で画面が真っ白（応答なし）になった。
- **解決策**: Burp Suite側で `Intercept is off` に切り替え、HTTPリクエストを正常にフォワード（透過）させることで解決。

### 🎯 次回の予定
- 登録したアカウントを用いたログイン挙動の確認
- Burp Suite（HTTP history等）を用いた通信の解析と、実際の脆弱性（OWASP Top 10ベース）の探索・攻略開始
