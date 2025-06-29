import nmap
from helpers import print_status, extract_os_info

def scan_ports(target):
    print_status(f"Scanning target: {target}...", "info")
    scanner = nmap.PortScanner()

    try:
        scanner.scan(hosts=target, arguments='-sS -sV -O')
        host_status = "Up" if scanner.all_hosts() else "Unreachable"

        if not scanner.all_hosts():
            print_status("No response from target.", "warn")
            return [], "Unknown", "Unknown", host_status

        os_guess, hostname = extract_os_info(scanner, target)

        ports = []
        for proto in scanner[target].all_protocols():
            for port in scanner[target][proto]:
                port_info = scanner[target][proto][port]
                ports.append({
                    "port": port,
                    "protocol": proto,
                    "state": port_info.get("state", "-"),
                    "service": port_info.get("name", "-"),
                    "version": port_info.get("version", "-"),
                })

        print_status("Port Scan completed.", "ok")
        print("\n")
        return ports, os_guess, hostname, host_status

    except Exception as e:
        print_status(f"Port scan error: {e}", "fail")
        return [], "Unknown", "Unknown", "Unreachable"
