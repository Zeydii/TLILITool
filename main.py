from scanner import port_scanner, vuln_scanner, dir_bruteforce, service_enum, output_formatter, subdomain_enum
from helpers import show_banner, print_status
import time

def main():
    show_banner()
    print_status("TLILITool - Aggressive Multi-Protocol Scanner", "info")
    time.sleep(1)

    target_input = input("Enter target IP or domain (optionally :port): ").strip()

    if ":" in target_input:
        target, port = target_input.split(":")
    else:
        target = target_input
        port = None

    print_status("Starting Port Scan...", "info")
    ports, os_guess, hostname, host_status = port_scanner.scan_ports(target)
    output_formatter.print_target_info(target, os_guess, hostname, host_status)

    if ports:
        output_formatter.print_port_results(ports)
    else:
        print_status("No open ports found or scan failed.", "warn")

    print_status("Running Vulnerability Scan...", "info")
    vuln_results = vuln_scanner.run_vuln_scan(target)
    output_formatter.print_vuln_results(vuln_results)

    print_status("Starting Directory Bruteforce with Gobuster...", "info")
    dir_results = dir_bruteforce.run_gobuster(target, port)
    output_formatter.print_dir_results(dir_results)

    print_status("Enumerating Services...", "info")
    service_enum.check_ftp(target)
    service_enum.check_http(target)
    print_status("Checking SMB shares...", "info")
    smb_shares = service_enum.check_smb_shares(target)
    if smb_shares:
        print_status(f"Found SMB shares:", "ok")
        for share in smb_shares:
            print(f" - {share}")
    else:
        print_status("No SMB shares found or SMB not accessible.", "warn")


    domain = input("Enter domain for subdomain enumeration (or leave blank to skip): ").strip()
    if domain:
        print_status(f"Enumerating subdomains for {domain}...", "info")
        subs = subdomain_enum.enumerate_subdomains(domain)
        output_formatter.print_subdomains(subs)

    print_status("Scan Completed. Review results above.", "ok")

if __name__ == "__main__":
    main()

