import requests
from colorama import Fore, Style

SECURITY_HEADERS = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Frame-Options",
    "X-Content-Type-Options"
]

def check_headers(url):

    print(f"\n{Fore.BLUE}[+] Checking Security Headers...{Style.RESET_ALL}\n")

    missing_headers = []

    try:

        response = requests.get(url, timeout=5)

        headers = response.headers

        for header in SECURITY_HEADERS:

            if header in headers:

                print(
                    f"{Fore.GREEN}[FOUND]{Style.RESET_ALL} {header}"
                )

            else:

                print(
                    f"{Fore.RED}[MISSING]{Style.RESET_ALL} {header}"
                )

                missing_headers.append(header)

    except Exception as e:

        print(f"{Fore.RED}Error:{Style.RESET_ALL} {e}")

    return missing_headers
