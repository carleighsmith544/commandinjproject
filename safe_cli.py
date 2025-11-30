# safe_cli.py
import re
import subprocess

# Allow only letters, digits, dots, and hyphens in the hostname or IP address
SAFE_TARGET_PATTERN = re.compile(r"^[a-zA-Z0-9\.\-]+$")

def is_safe_target(target: str) -> bool:
    """
    Whitelist validation:
    - Only letters, digits, dots, and hyphens are allowed.
    - No spaces, no &, no |, no ;, etc.
    """
    return bool(SAFE_TARGET_PATTERN.fullmatch(target))

def main():
    print("=== Safe Ping Tool (Windows) ===")
    target = input("Enter an IP address or hostname to ping: ").strip()

    # 1. Validate the input using a whitelist
    if not is_safe_target(target):
        print("\n[ERROR] Invalid input.")
        print("[INFO] Only letters, digits, dots, and hyphens are allowed.")
        print("[INFO] This prevents special characters from being interpreted as commands.")
        return

    # 2. Build the command as a list of arguments (no shell)
    cmd = ["ping", "-n", "2", target]

    print(f"\n[DEBUG] Running command safely with arguments: {cmd}\n")

    try:
        # 3. Use subprocess.run with shell=False so the shell does not interpret the string
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=False
        )
        print(result.stdout)
        if result.stderr:
            print("[stderr]")
            print(result.stderr)
    except FileNotFoundError:
        print("[ERROR] Ping command not found on this system.")
    except Exception as e:
        print(f"[ERROR] Unexpected problem: {e}")

if __name__ == "__main__":
    main()
