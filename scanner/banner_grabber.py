import socket
from colorama import Fore, Style

def grab_banner(target, port):

    try:
        s = socket.socket()
        s.settimeout(2)

        s.connect((target, port))

        banner = s.recv(1024).decode().strip()

        print(
            f"{Fore.MAGENTA}[SERVICE]{Style.RESET_ALL} "
            f"Port {port} → {banner}"
        )

        s.close()

        return banner

    except:
        return None
