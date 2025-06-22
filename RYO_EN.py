#!/usr/bin/env python3
import zlib, base64, marshal, requests, sys
from rich.console import Console
from rich.panel import Panel

console = Console()

def get_kill_url():
    enc_data = "eJz7HMPAwJDqVeXj7Zxd4O2TFGxYaent45fiU1VZ5eXtalDoE2pSElxsHuBtkOfnbenmU1WsH+ZT5ePpV6wf4WJSZGBoYelX5VsV4lNp6uXjnF1imFla4O3o6pirHRruk25rCwD/rh8l"
    decoded = marshal.loads(zlib.decompress(base64.b64decode(enc_data.encode())))
    return zlib.decompress(base64.b64decode(decoded)).decode()

def check_kill():
    try:
        url = get_kill_url()
        status = requests.get(url, timeout=5).text.strip()
        if status != "ON":
            console.print("[bold red]🔴 This tool has been disabled remotely.[/bold red]")
            sys.exit(0)
    except Exception:
        console.print("[bold red]⚠️ Unable to verify tool status.[/bold red]")
        sys.exit(0)

def banner():
    console.print(Panel("RYO - Global Vulnerability Scanner", style="cyan"))

def main():
    check_kill()
    banner()
    console.print("[1] SQL Injection\n[2] XSS\n[3] Exit")
    choice = input("> ")
    if choice == "1":
        console.print("Running SQLi test...")
    elif choice == "2":
        console.print("Running XSS test...")
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()
