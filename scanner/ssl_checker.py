import ssl
import socket

from colorama import Fore, Style


def check_ssl(target):

    print(
        f"\n{Fore.CYAN}[+] SSL Certificate Analysis:"
        f"{Style.RESET_ALL}\n"
    )

    try:

        context = ssl.create_default_context()

        with socket.create_connection(
            (target, 443)
        ) as sock:

            with context.wrap_socket(
                sock,
                server_hostname=target
            ) as ssock:

                cert = ssock.getpeercert()

                issuer = cert['issuer']

                expiry = cert['notAfter']

                print(
                    f"{Fore.GREEN}[SSL ACTIVE]"
                    f"{Style.RESET_ALL}"
                )

                print(f"Issuer: {issuer}")
                print(f"Expiry: {expiry}")

                return {
                    "issuer": issuer,
                    "expiry": expiry
                }

    except Exception as e:

        print(
            f"{Fore.RED}[SSL ERROR]"
            f"{Style.RESET_ALL} {e}"
        )

        return None
