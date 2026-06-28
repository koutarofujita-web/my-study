# TryHackMe 学習記録: Blue（偵察編）

## 🎯 今日の目標
TryHackMeの「Blue」の部屋に参加し、
ターゲットマシンの偵察（情報収集）を行う。

## 🛠 使用したツール・環境
- TryHackMe AttackBox (Linux環境)
- nmap (ポートスキャン・脆弱性診断ツール)

## ✍️ 実施内容と手順

### 1. ターゲットマシンの偵察（ポートスキャン）
ターゲットIPに対して、サービスバージョンの検出、Ping省略（`-Pn`）、
詳細出力（`-v`）、および脆弱性スキャンスクリプト（`--script vuln`）を指定して `nmap` を実行した。

```bash
nmap -sV -Pn -oN nmap.txt -v <ターゲットIP> --script vuln
