# Backup Manager (CLI & Web App)

Linux環境向けに開発した、対話型のバックアップ管理ツールおよびWebダッシュボード

## 本日の開発成果
- **CLIツールの高度化 (v3.0)**
  - `config.conf` による設定保持機能の実装
  - システム状態（ディスク空き容量、`rsync`インストール状況）の動的取得
  - カラー表示（ANSIエスケープシーケンス）によるUIの視認性向上
  - ログ記録機能（`backup.log`）の導入とメニューからの閲覧機能
- **Webアプリケーション化への移植（第一歩）**
  - Python (Flask) を用いたローカルWebサーバーの立ち上げ
  - シェルスクリプト側で取得していたシステム状態情報をPython経由で読み込み、ブラウザ（`http://localhost:5000`）へダッシュボード表示

## 使用技術 / 環境
- OS: Linux (Chromebook / Crostini)
- Shell: Bash
- Language: Python 3
- Web Framework: Flask
