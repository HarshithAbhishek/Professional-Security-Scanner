import requests

security_headers = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Frame-Options",
    "X-Content-Type-Options"
]

def check_headers(url):

    print("\n[+] Checking Security Headers...\n")

    missing_headers = []

    try:
        response = requests.get(url)

        headers = response.headers

        for header in security_headers:

            if header in headers:
                print(f"[FOUND] {header}")
            else:
                print(f"[MISSING] {header}")
                missing_headers.append(header)

    except:
        print("Error connecting to website")

    return missing_headers
