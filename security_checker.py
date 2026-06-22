import os
import stat

TARGET_DIR = os.path.expanduser("~/")
SSH_CONFIG_PATH = "/etc/ssh/sshd_config"

print("=" * 55)
print("[🛡️ SECURITY CHECKER v1.1] 高度Linuxセキュリティ診断 開始...")
print("=" * 55)

# 危険度ごとにカウントする箱を用意
stats = {"HIGH": 0, "MEDIUM": 0, "LOW": 0}

print("[1] フォルダ内のパーミッション詳細チェック中...")
for root, dirs, files in os.walk(TARGET_DIR):
    for file in files:
        file_path = os.path.join(root, file)
        try:
            file_stat = os.stat(file_path)
            permissions = file_stat.st_mode
           
            # 🔴 危険度：高 (HIGH) -> 誰でも読み書き実行ができる「777」
            if (permissions & stat.S_IRWXO) == stat.S_IRWXO and (permissions & stat.S_IRWXG) == stat.S_IRWXG:
                print(f"🔴 [HIGH] 危険な権限(777)を検知 -> {file_path}")
                stats["HIGH"] += 1
               
            # 🟡 危険度：中 (MEDIUM) -> グループや他人が書き込みできる「755」や「666」など（簡易判定）
            elif (permissions & stat.S_IWOTH) or (permissions & stat.S_IWGRP):
                # ただし、自分がさっき直した「644」などの安全なものは除外する
                print(f"🟡 [MEDIUM] 緩い書き込み権限を検知 -> {file_path}")
                stats["MEDIUM"] += 1

        except Exception:
            continue

print("\n[2] システムの設定ファイルチェック中...")
if os.path.exists(SSH_CONFIG_PATH):
    try:
        with open(SSH_CONFIG_PATH, "r") as f:
            for line in f:
                if line.strip().startswith("PermitRootLogin") and "yes" in line:
                    print(f"🔴 [HIGH] root直接ログインが許可されています！ -> {SSH_CONFIG_PATH}")
                    stats["HIGH"] += 1
    except Exception:
        print(f"[*] 設定ファイルの読み込みスキップ (権限なし)")
else:
    # 🔵 危険度：低 (LOW) -> テスト環境特有の通知など
    print(f"🔵 [LOW] 本物のSSH設定ファイルがないため、疑似環境としてスキップします。")
    stats["LOW"] += 1

print("=" * 55)
print("[📊 診断結果レポート]")
print(f"  🔴 緊急対処 (HIGH)  : {stats['HIGH']} 件")
print(f"  🟡 要注意   (MEDIUM): {stats['MEDIUM']} 件")
print(f"  🔵 要確認   (LOW)   : {stats['LOW']} 件")
print("=" * 55)
print("[🛡️] 診断が完了しました。")
print("=" * 55)
