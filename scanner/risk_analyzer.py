from colorama import Fore, Style

RISKY_PORTS = {
    21: "FTP - Insecure file transfer protocol",
    23: "Telnet - Unencrypted remote access",
    25: "SMTP - Possible mail abuse",
    110: "POP3 - Unencrypted email access",
    139: "NetBIOS - Vulnerable Windows service",
    445: "SMB - Common ransomware target"
}

def analyze_risks(open_ports):

    print(f"\n{Fore.RED}[+] Risk Analysis:{Style.RESET_ALL}\n")

    risks_found = []

    for item in open_ports:

        port = item['port']

        if port in RISKY_PORTS:

            risk = RISKY_PORTS[port]

            print(
                f"{Fore.RED}[HIGH RISK]{Style.RESET_ALL} "
                f"Port {port} → {risk}"
            )

            risks_found.append({
                "port": port,
                "risk": risk
            })

    if not risks_found:

        print(
            f"{Fore.GREEN}No major risks detected"
            f"{Style.RESET_ALL}"
        )

    return risks_found
