import sys
from datetime import date

# 確保在 Windows 終端機能正常印出 Unicode 與表情符號
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

def main():
    username = "411512015-jpg"
    print(f"Hello, GitHub! I am {username}.")
    print(f"Today is: {date.today()}")
    print("祝你有美好的一天！✨")

if __name__ == "__main__":
    main()
