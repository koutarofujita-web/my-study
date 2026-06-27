# 学習記録：ChromebookへのKali Linux環境構築とポートスキャン（nmap）の実践

## 📝 今日学んだこと（概要）
- Chromebook（Debian最新環境）におけるAPTリポジトリの公開鍵管理ルール（旧 `apt-key` 廃止への対応）
- ポートスキャンツール `nmap` の導入と基本的な偵察コマンドの習得
- TryHackMe環境でのターゲットマシンの起動と偵察の流れの理解

---

## 🛠️ 1. Chromebook（Linux環境）での環境構築

### 発生した課題
最新のDebian環境ではセキュリティの脆弱性対策のため、古い `apt-key` コマンドが廃止されていた。
そのため、書籍通りの古い方法でKali Linuxのリポジトリを追加しようとすると、公開鍵の検証エラー（`Missing key` / `署名されていません`）が発生した。

### 解決策（最新の個別管理ルールへの対応）
各リポジトリの公開鍵を共通キーリングに混ぜず、専用の場所に隔離して保存し、ソースリスト側で `[signed-by=...]` を指定して紐付ける方法で解決した。

```bash
# 1. エラーになった古い設定の削除
sudo rm /etc/apt/sources.list.d/kali.list

# 2. 安全なディレクトリにKali公式の公開鍵をダウンロード
sudo wget -q -O /usr/share/keyrings/kali-archive-keyring.gpg [https://archive.kali.org/archive-key.asc](https://archive.kali.org/archive-key.asc)

# 3. 鍵を明示的に指定してリポジトリを登録
echo "deb [signed-by=/usr/share/keyrings/kali-archive-keyring.gpg]
[http://http.kali.org/kali](http://http.kali.org/kali) kali-rolling main contrib non-free non-free-firmware" | sudo tee /etc/apt/sources.list.d/kali.list

# 4. アップデートの実行とnmapのインストール
sudo apt update
sudo apt install -y nmap
