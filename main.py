import socket
from colorama import Fore, Style, init

from scanner.port_scanner import scan_ports
from scanner.risk_analyzer import analyze_risks
from scanner.header_checker import check_headers
from scanner.report_generator import generate_html_report
from scanner.cve_checker import check_cves
# Initialize colorama
init()

print(f"""{Fore.RED}

========================================
        SECURITY SCANNER
========================================

{Style.RESET_ALL}
""")

# User input
target = input("Enter target website or IP: ")

try:
    # Convert domain to IP
    target_ip = socket.gethostbyname(target)

    print(f"\n{Fore.YELLOW}[TARGET]{Style.RESET_ALL} {target}")
    print(f"{Fore.YELLOW}[IP]{Style.RESET_ALL} {target_ip}")

except:
    print(f"{Fore.RED}Invalid Target{Style.RESET_ALL}")
    exit()

# Run port scanner
open_ports = scan_ports(target_ip)

print(f"\n{Fore.CYAN}[+] Scan Completed{Style.RESET_ALL}")

print(f"\n{Fore.GREEN}[+] Open Ports Found:{Style.RESET_ALL}")

# Display results
for item in open_ports:

    print(f"\n - Port {item['port']}")
    print(f"   Service: {item['banner']}")
# Analyze risks
risks = analyze_risks(open_ports)
# Check website security headers
url = f"http://{target}"

missing_headers = check_headers(url)
# Check for known vulnerabilities
detected_cves = check_cves(open_ports)
# Generate HTML report
generate_html_report(
    target,
    open_ports,
    risks,
    missing_headers
)
