import hashlib, os
F = "important_data.txt"

def get_h():
    if not os.path.exists(F): return ""
    with open(F, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

mode = input("1:Save 2:Check -> ")
if mode == "1":
    with open("master.txt", "w") as f: f.write(get_h())
    print("Saved!")
elif mode == "2":
    with open("master.txt", "r") as f: m = f.read()
    now = get_h()
    print("OK" if now == m else "ALERT!!!")
