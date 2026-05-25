def generate_report(target, open_ports, missing_headers):

    with open("report.txt", "w") as report:

        report.write("VULNERABILITY SCAN REPORT\n")
        report.write("=" * 40 + "\n\n")

        report.write(f"Target: {target}\n\n")

        report.write("OPEN PORTS:\n")

        for port in open_ports:
            report.write(f"- Port {port} OPEN\n")

        report.write("\nMISSING SECURITY HEADERS:\n")

        for header in missing_headers:
            report.write(f"- {header}\n")

    print("\n[+] Report saved as report.txt")
