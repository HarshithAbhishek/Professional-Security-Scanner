from colorama import Fore, Style

# Simple CVE database
CVE_DATABASE = {

    "Apache/2.4.49": {
        "cve": "CVE-2021-41773",
        "severity": "CRITICAL",
        "description": "Path traversal vulnerability in Apache HTTP Server"
    },

    "OpenSSH_7.2": {
        "cve": "CVE-2016-0777",
        "severity": "HIGH",
        "description": "Information disclosure vulnerability in OpenSSH"
    }

}

def check_cves(open_ports):

    print(f"\n{Fore.MAGENTA}[+] CVE Analysis:{Style.RESET_ALL}\n")

    detected_cves = []

    for item in open_ports:

        banner = item['banner']

        if not banner:
            continue

        for service in CVE_DATABASE:

            if service.lower() in banner.lower():

                vuln = CVE_DATABASE[service]

                print(
                    f"{Fore.RED}[{vuln['severity']}]{Style.RESET_ALL} "
                    f"{vuln['cve']}"
                )

                print(
                    f"Service: {banner}"
                )

                print(
                    f"Issue: {vuln['description']}\n"
                )

                detected_cves.append({
                    "service": banner,
                    "cve": vuln['cve'],
                    "severity": vuln['severity'],
                    "description": vuln['description']
                })

    if not detected_cves:

        print(
            f"{Fore.GREEN}No known CVEs detected"
            f"{Style.RESET_ALL}"
        )

    return detected_cves
