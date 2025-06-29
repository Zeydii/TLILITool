from colorama import Fore, Style

def print_target_info(target, os_guess, hostname, status):
    print(f"{Fore.CYAN}[+] Host Information:{Style.RESET_ALL}")
    print(f"    - IP Address   : {target}")
    print(f"    - Hostname     : {hostname if hostname else 'Unknown'}")
    print(f"    - OS Guess     : {os_guess if os_guess else 'Unknown'}")
    print(f"    - Host Status  : {status}\n")

def print_port_results(ports):
    if not ports:
        print(f"{Fore.YELLOW}[!] No open ports found or scan failed.{Style.RESET_ALL}\n")
        return

    print(f"{Fore.CYAN}[+] Port Scan Results:{Style.RESET_ALL}")
    print("    ┌───────┬───────────┬────────┬──────────────┬─────────────┐")
    print("    │ Port  │ Protocol  │ State  │ Service      │ Version     │")
    print("    ├───────┼───────────┼────────┼──────────────┼─────────────┤")
    for port_info in ports:
        port = port_info.get("port", "-")
        protocol = port_info.get("protocol", "-")
        state = port_info.get("state", "-")
        service = port_info.get("service", "-")
        version = port_info.get("version", "-")
        print(f"    │ {str(port).ljust(5)} │ {protocol.ljust(9)} │ {state.ljust(6)} │ {service.ljust(12)} │ {version.ljust(11)} │")
    print("    └───────┴───────────┴────────┴──────────────┴─────────────┘\n")

def print_vuln_results(results):
    print("\n[+] Port-Level Vulnerability Scan Results:\n")
    if not results:
        print("    No vulnerabilities detected.\n")
        return

    for r in results:
        print(f"    - Port {r['port']} ({r['service']}): {r['product']} {r['version']}")
        if r['cves']:
            for cve in r['cves']:
                print(f"        * {cve}")
        else:
            print(f"        * No CVEs detected.")
    print()

def print_smb_results(anon_allowed, shares):
    print(f"{Fore.CYAN}[+] SMB Share Check:{Style.RESET_ALL}")
    anon_status = "Allowed" if anon_allowed else "Not Allowed"
    print(f"    - Anonymous Login: {anon_status}")

    if shares:
        print("    - Available Shares:")
        for share in shares:
            print(f"        - {share}")
    else:
        print("    - No shares found or SMB not accessible.")
    print()

def print_dir_results(dirs):
    if not dirs:
        print(f"{Fore.YELLOW}[!] No directory bruteforce results to display.{Style.RESET_ALL}\n")
        return

    print(f"{Fore.CYAN}[+] Directory Bruteforce Results:{Style.RESET_ALL}")
    for path in dirs:
        print(f"    {path}")
    print()

def print_subdomains(subs):
    if not subs:
        print(f"{Fore.YELLOW}[!] No subdomains found.{Style.RESET_ALL}\n")
        return

    print(f"{Fore.CYAN}[+] Subdomain Enumeration Results:{Style.RESET_ALL}")
    for sub in subs:
        print(f"    - {sub}")
    print()
