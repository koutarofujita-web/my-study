# 🛡️ SIEM (Security Information and Event Management) 分析ツールの開発基盤構築

SIEM風ログ分析ツールの構築に向けた、Docker環境およびインメモリデータベース（Redis）によるログ処理基盤のセットアップログです。

---

## 🛠️ 本日実施したこと

### 1. 開発コンテナ環境の構築（Docker / Docker Compose）
* **コンテナ構成の設計**
  * 高速な状態管理・イベント処理に利用する **Redis 7 (Alpine)** コンテナのセットアップ
  * ログの集計・処理を担う **Python 3.11 (Slim)** アプリケーションコンテナの作成
* **環境分離と永続化**
  * `docker-compose.yml` を用いたマルチコンテナ連携設定
  * Redis Volume定義によるデータの永続化設定

### 2. アプリケーション実行環境のセットアップ
* `Dockerfile` を作成し、ログ分析に必要な Python 依存パッケージ（`redis`）を自動インストールするビルド環境を整備
* Linux環境上でのパーミッション調整および `docker-compose up --build` によるコンテナ起動・疎通確認

---

## 📁 ディレクトリ構造
```text
siem-engine/
├── Dockerfile          # Pythonアプリケーション実行環境の定義
├── docker-compose.yml  # RedisおよびAppコンテナのマルチサービス構成
└── main.py             # ログ処理エントリーポイント
