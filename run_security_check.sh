#!/bin/bash

# 1. 出力ファイルの設定
OUTPUT_FILE="/home/koutarou/security_report.txt"
CHECK_DATE=$(date '+%Y-%m-%d_%H:%M:%S')

echo "============================================================" > "$OUTPUT_FILE"
echo "              SECURITY DIAGNOSTIC REPORT                    " >> "$OUTPUT_FILE"
echo "              DATE: $CHECK_DATE                             " >> "$OUTPUT_FILE"
echo "============================================================" >> "$OUTPUT_FILE"

# 2. 簡易システム診断（例としてポート確認など）のログを記録
echo "[1] ネットワークポート状態:" >> "$OUTPUT_FILE"
ss -tulpn >> "$OUTPUT_FILE" 2>&1
echo "" >> "$OUTPUT_FILE"

echo "[2] ディスク使用量:" >> "$OUTPUT_FILE"
df -h >> "$OUTPUT_FILE" >> "$OUTPUT_FILE" 2>&1
echo "" >> "$OUTPUT_FILE"

# 3. USBメモリへのバックアップ（マウントされていればコピー）
USB_PATH="/mnt/chromeos/removable/USB DISK 3.2"
if [ -d "$USB_PATH" ]; then
    cp "$OUTPUT_FILE" "$USB_PATH/security_report_${CHECK_DATE}.txt"
    echo "★USBへのコピーも成功しました！" >> "$OUTPUT_FILE"
fi

echo "============================================================" >> "$OUTPUT_FILE"
echo "診断完了" >> "$OUTPUT_FILE"
