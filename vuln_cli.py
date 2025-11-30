# vuln_cli.py
import os

def main():
    print("=== Vulnerable Ping Tool (Windows) ===")
    target = input("Enter an IP address or hostname to ping: ")

    # VULNERABLE: user input is inserted directly into a shell command string
    command = f"ping -n 2 {target}"  # -n is the Windows option for number of pings
    print(f"\n[DEBUG] Running command: {command}\n")

    # os.system passes the command to the system shell, which will interpret special characters
    os.system(command)

if __name__ == "__main__":
    main()
