from colorama import Fore, Style


def calculate_threat_score(
    open_ports,
    risks,
    missing_headers
):

    score = 0

    # Open ports
    score += len(open_ports) * 5

    # Risks
    score += len(risks) * 20

    # Missing headers
    score += len(missing_headers) * 10

    # Classification
    if score >= 70:

        level = "HIGH"

        color = Fore.RED

    elif score >= 40:

        level = "MEDIUM"

        color = Fore.YELLOW

    else:

        level = "LOW"

        color = Fore.GREEN

    print(
        f"\n{color}[THREAT SCORE]"
        f"{Style.RESET_ALL} {score}"
    )

    print(
        f"{color}[RISK LEVEL]"
        f"{Style.RESET_ALL} {level}"
    )

    return {
        "score": score,
        "level": level
    }
