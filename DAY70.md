# Simple Bash Backup Manager

シェルスクリプト（Bash）で動作する、軽量かつ実用的でログ出力機能を備えた自動バックアップ管理ツールです。  
指定フォルダの差分バックアップを行い、過去の不要なバックアップフォルダを自動で検索・削除します。

## 💡 特徴 (Features)

- **日時付きフォルダ作成**: バックアップ実行時のタイムスタンプ（`YYYYMMDD_HHMMSS`）を付与して保存します。
- **rsync による差分転送**: 効率的なファイルコピーを行うため、大容量データのバックアップにも適しています。
- **古いデータの自動削除**: `find` コマンドを使用し、指定日数（デフォルト: 7日）を経過した旧バックアップを自動でクリーンアップします。
- **詳細なログ出力**: 実行結果やコピーされたファイルリストを日時付きで `backup.log` に記録・管理できます。

## 🛠 動作要件 (Requirements)

- OS: Linux / macOS / WSL (Windows Subsystem for Linux)
- Bash 4.0 以上
- `rsync`

※ `rsync` が未インストールの場合は、事前に以下でインストールしてください。
```bash
sudo apt update && sudo apt install -y rsync
