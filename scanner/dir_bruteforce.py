import subprocess
from helpers import print_status

def run_gobuster(target, port=None):
    print_status(f"Starting Gobuster on {target}...", "info")
    results = []

    url = f"http://{target}"
    if port:
        url = f"http://{target}:{port}"

    try:
        cmd = ["gobuster", "dir", "-u", url, "-w", "/usr/share/wordlists/dirb/common.txt", "-q"]
        process = subprocess.run(cmd, capture_output=True, text=True)

        if process.returncode != 0:
            print_status(f"Gobuster error: {process.stderr.strip()}", "fail")
            return results

        lines = process.stdout.strip().split("\n")
        for line in lines:
            results.append(line)

        print_status("Directory bruteforce completed.", "ok")
        return results

    except Exception as e:
        print_status(f"Directory bruteforce error: {e}", "fail")
        return results

