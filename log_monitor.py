import time
import os

# 【ルートA】本物のLinuxの認証ログを指定
LOG_FILE_PATH = "test_auth.log"

def real_time_monitor():
    print(f"[*] {LOG_FILE_PATH} のリアルタイム監視を開始しました...")
    print("[-] 終了するには Ctrl + C を押してください。\n")

    # カウンターの初期化
    login_failures = 0
    sudo_executions = 0
    ssh_connections = 0

    # まず、今あるファイルの「一番最後の行」までワープする（ルートBの仕込み）
    if os.path.exists(LOG_FILE_PATH):
        file_size = os.path.getsize(LOG_FILE_PATH)
    else:
        print(f"エラー: {LOG_FILE_PATH} が見つかりません。")
        return

    try:
        with open(LOG_FILE_PATH, "r", encoding="utf-8", errors="ignore") as f:
            # ファイルの末尾に移動（起動した「あと」のログだけをリアルタイムに追記監視するため）
            f.seek(file_size)

            # 【ルートB】無限ループで新しい行が来るのをずっと待ち構える
            while True:
                line = f.readline()
               
                # 新しい行がない場合は、0.1秒待ってから再確認（PCの負担を減らす）
                if not line:
                    time.sleep(0.1)
                    continue

                # 新しいログが1行来たら、キーワードをチェックしてカウント
                found_something = False

                if "authentication failure" in line or "Failed password" in line:
                    login_failures += 1
                    found_something = True
               
                if "COMMAND=" in line:
                    sudo_executions += 1
                    found_something = True
               
                if "sshd" in line and "Accepted" in line:
                    ssh_connections += 1
                    found_something = True

                # 何か検知したら、その瞬間に画面を更新して表示
                if found_something:
                    print("\n===== 🚨 ログ検知（リアルタイム） =====")
                    print(f"ログイン失敗回数 : {login_failures} 回")
                    print(f"sudo実行回数     : {sudo_executions} 回")
                    print(f"SSH接続成功回数  : {ssh_connections} 回")
                    print("=======================================")

    except KeyboardInterrupt:
        print("\n[*] 監視を終了しました。お疲れ様でした！")
    except PermissionError:
        print("\n[!] エラー: 本物のログを読むには管理者権限が必要です。")
        print("[!] 'sudo python3 log_monitor.py' で実行してください。")

if __name__ == "__main__":
    real_time_monitor()
