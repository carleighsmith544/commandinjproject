# Punching Holes in the Shell  
_A command injection demo and secure coding walkthrough_

## Overview

This project demonstrates how a simple Python command-line program can become vulnerable to **command injection**, and how a few secure coding practices can completely remove the vulnerability.

We implement two versions of a ping utility:

- `vuln_cli.py` – **intentionally vulnerable** version that uses `os.system()` with unvalidated user input.
- `safe_cli.py` – **fixed** version that uses whitelist validation and `subprocess.run(shell=False)` to block command injection.

The project was created for a security-focused final project to show both the attack and the defense in a clear, testable way.

---

## Project Structure

```text
Punching-Holes-In-The-Shell/
├─ vuln_cli.py     # Vulnerable ping tool (demo of command injection)
├─ safe_cli.py     # Patched ping tool (secure version)
└─ README.md       # Project documentation


How to Run the Vulnerable Demo
1. Open a Terminal

Open Command Prompt and navigate to the project folder:

cd "C:\path\to\Punching-Holes-In-The-Shell"

2. Run the Vulnerable Script
python vuln_cli.py

3. Normal Behavior (No Attack)

When prompted:

Enter an IP address or hostname to ping:


enter a normal IP, e.g.:

8.8.8.8

You should see normal ping output.

4. Command Injection Attack (Demo Only)

Run the script again:

python vuln_cli.py

This time, enter:

8.8.8.8 && echo INJECTION SUCCESSFUL

The program builds and executes:

ping -n 2 8.8.8.8 && echo INJECTION SUCCESSFUL

Because os.system() sends the whole string to the Windows shell, the && operator lets an attacker run another command. You should see ping output plus:

INJECTION SUCCESSFUL


This demonstrates a command injection vulnerability: the program appears to just ping a host, but it actually allows arbitrary shell commands to run.

How to Run the Fixed (Secure) Demo

1. Run the Secure Script
python safe_cli.py

2. Normal Input

Enter:

8.8.8.8

You should again see normal ping output. The secure version still behaves correctly for valid input.

3. Reuse the Attack Payload

Run again:

python safe_cli.py

Enter the same attack string:

8.8.8.8 && echo INJECTION SUCCESSFUL

Now the program should show an error similar to:

[ERROR] Invalid input.
[INFO] Only letters, digits, dots, and hyphens are allowed.
[INFO] This prevents special characters from being interpreted as commands.

No ping runs, and no extra command runs. The attack is blocked.
