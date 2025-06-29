import subprocess
from helpers import print_status

def enumerate_subdomains(target):
    subdomains = []
    print_status(f"Enumerating subdomains for {target}...", "info")
    try:
        result = subprocess.check_output(["sublist3r", "-d", target], text=True)
        for line in result.splitlines():
            if line.startswith("[-] ") and "Found" not in line:
                subdomain = line.split()[-1]
                subdomains.append(subdomain)
    except Exception as e:
        print_status(f"Subdomain enumeration failed: {e}", "fail")

    return subdomains

# output_formatter.py
from colorama import Fore, Style

def print_target_info(target_ip, os_guess, hostname):
    print(f"\n{Fore.MAGENTA}{Style.BRIGHT}╔══════════════════════════════════════╗")
    print(f"║       {Fore.CYAN}Scan Results for: {target_ip}{Fore.MAGENTA}       ║")
    print(f"╚══════════════════════════════════════╝{Style.RESET_ALL}\n")
    print(f"{Fore.GREEN}Host Status  : {Fore.WHITE}up")
    print(f"{Fore.GREEN}Detected OS  : {Fore.WHITE}{os_guess}")
    print(f"{Fore.GREEN}Hostname     : {Fore.WHITE}{hostname}\n")

def print_port_results(ports):
    if not ports:
        print(f"{Fore.YELLOW}[!] No ports open or detected.")
        return
    header = f"{Fore.CYAN}{'Port':<8}{'Protocol':<10}{'State':<8}{'Service':<12}{'Version':<10}"
    print(header)
    print(f"{Fore.CYAN}{'-'*48}")
    for port in ports:
        print(f"{Fore.WHITE}{port['port']:<8}{'tcp':<10}{port['state']:<8}{port['service']:<12}{port['version']:<10}")

def print_subdomains(subdomains):
    if not subdomains:
        print(f"\n{Fore.YELLOW}[!] No subdomains found.")
        return
    print(f"\n{Fore.GREEN}[+] Discovered Subdomains:\n")
    for sub in subdomains:
        print(f" - {sub}")

