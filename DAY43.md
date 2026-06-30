# 学習記録：
2026-06-29

## 🎯 本日の目標
* TryHackMeの「Blue」の部屋を攻略し、Windowsマシンの脆弱性を突く一連の流れを理解する。

## 💻 実施内容
### 1. Metasploitを使ったエクスプロイトの実行
* ターゲット（Windows 7）の脆弱性「MS17-010（EternalBlue）」を悪用するモジュールを選択。
* `RHOSTS`（ターゲットIP）および `LHOST`（自身のAttackBoxのIP）を正しく設定し、エクスプロイトを実行。
* ペイロードには `windows/x64/meterpreter/reverse_tcp` を使用。

### 2. アクセス権の取得（Gain Access）
* エクスプロイトに成功し、`meterpreter >` セッションを確立。
* `sysinfo` コマンドを実行し、ターゲットのOS情報（Windows 7）やコンピュータ名（JON-PC）などの内部情報を正常に取得。
* TryHackMeのタスク2のクイズ（完全なパス：`exploit/windows/smb/ms17_010_eternalblue`、必須オプション：`RHOSTS`）を
  すべてクリア。

### 3. 環境構築とトラブルシューティング
* 無料プランのAttackBox利用制限（1日1時間）に伴うエラーに直面。
* 回避策として、ローカル環境（ChromebookのLinux環境）からOpenVPN経由でTryHackMeの
  ネットワークに直接接続するための設定（`.ovpn` ファイルのダウンロードと適用）を実施。

## 💡 わかったこと・反省点
* 設定値のタイポ（`PHOSTS` など）があると当然エラーになるため、変数の確認が重要。
* AttackBoxの制限があっても、OpenVPNを使って自分のローカル端末から接続すれば、
  無料のまま検証環境を継続できる。インフラやネットワーク接続の仕組みを学ぶ良いきっかけになった。
