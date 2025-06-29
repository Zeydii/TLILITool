from helpers import print_status
import nmap

def run_vuln_scan(target):
    print_status(f"Running vulnerability scan on {target}...", "info")
    scanner = nmap.PortScanner()
    results = []

    try:
        scanner.scan(target, arguments="-sV --script vulners")

        for host in scanner.all_hosts():
            for port in scanner[host]['tcp']:
                service = scanner[host]['tcp'][port]
                product = service.get('product', '-')
                version = service.get('version', '-')
                script_output = service.get('script', {})

                cves = []
                if "vulners" in script_output:
                    lines = script_output["vulners"].splitlines()
                    for line in lines:
                        if "CVE-" in line:
                            cve = line.split()[0]
                            exploit_link = f"https://www.exploit-db.com/search?cve={cve}"
                            cves.append(f"{cve} ({exploit_link})")

                results.append({
                    "port": port,
                    "service": service.get('name', '-'),
                    "product": product,
                    "version": version,
                    "cves": cves
                })
                
        print_status("Vulnerability scan completed.", "ok")
        return results

    except Exception as e:
        print_status(f"Vulnerability scan error: {e}", "fail")
        return []

