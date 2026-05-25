import socket
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style

from scanner.banner_grabber import grab_banner

# Common ports to scan
COMMON_PORTS = [
    20, 21, 22, 23, 25,
    53, 80, 110, 139,
    143, 443, 445, 8080
]

def scan_single_port(target, port):

    try:
        # Create socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set timeout
        s.settimeout(1)

        # Attempt connection
        result = s.connect_ex((target, port))

        # If port is open
        if result == 0:

            print(f"{Fore.GREEN}[OPEN]{Style.RESET_ALL} Port {port}")

            # Grab service banner
            banner = grab_banner(target, port)

            return {
                "port": port,
                "banner": banner
            }

        s.close()

    except:
        pass

    return None


def scan_ports(target):

    print(f"\n{Fore.CYAN}[+] Starting Port Scan...{Style.RESET_ALL}\n")

    open_ports = []

    # Multithreaded scanning
    with ThreadPoolExecutor(max_workers=100) as executor:

        results = executor.map(
            lambda port: scan_single_port(target, port),
            COMMON_PORTS
        )

    # Store results
    for result in results:

        if result:
            open_ports.append(result)

    return open_ports
