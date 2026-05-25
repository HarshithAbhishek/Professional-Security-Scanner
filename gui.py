import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, filedialog
from tkinter.ttk import Progressbar

import ttkbootstrap as ttk

from scanner.port_scanner import scan_ports
from scanner.risk_analyzer import analyze_risks
from scanner.header_checker import check_headers
from scanner.cve_checker import check_cves
from scanner.ssl_checker import check_ssl
from scanner.threat_score import calculate_threat_score
from scanner.pdf_report import generate_pdf_report


# Save output manually
def save_report():

    content = output_box.get(1.0, tk.END)

    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[
            ("Text Files", "*.txt"),
            ("All Files", "*.*")
        ]
    )

    if file_path:

        with open(file_path, "w") as file:
            file.write(content)

        status_label.config(
            text="Report Saved Successfully"
        )


# Run scan in thread
def threaded_scan():

    threading.Thread(
        target=start_scan
    ).start()


# Main scan function
def start_scan():

    progress.start()

    output_box.delete(1.0, tk.END)

    target = target_entry.get()

    status_label.config(
        text="Scanning..."
    )

    try:

        target_ip = socket.gethostbyname(target)

    except:

        output_box.insert(
            tk.END,
            "Invalid Target\n"
        )

        progress.stop()

        return

    # Target info
    output_box.insert(
        tk.END,
        f"""
====================================
TARGET INFORMATION
====================================

Target: {target}
IP Address: {target_ip}

"""
    )

    # Port scan
    output_box.insert(
        tk.END,
        "\n[+] Running Port Scan...\n\n"
    )

    open_ports = scan_ports(target_ip)

    for item in open_ports:

        output_box.insert(
            tk.END,
            f"[OPEN] Port {item['port']} "
            f"→ {item['banner']}\n"
        )

    # Risk analysis
    output_box.insert(
        tk.END,
        "\n====================================\n"
        "RISK ANALYSIS\n"
        "====================================\n\n"
    )

    risks = analyze_risks(open_ports)

    if risks:

        for risk in risks:

            output_box.insert(
                tk.END,
                f"[HIGH RISK] "
                f"Port {risk['port']} → "
                f"{risk['risk']}\n"
            )

    else:

        output_box.insert(
            tk.END,
            "No major risks detected\n"
        )

    # SSL analysis
    output_box.insert(
        tk.END,
        "\n====================================\n"
        "SSL ANALYSIS\n"
        "====================================\n\n"
    )

    ssl_info = check_ssl(target)

    if ssl_info:

        output_box.insert(
            tk.END,
            f"Issuer: {ssl_info['issuer']}\n"
        )

        output_box.insert(
            tk.END,
            f"Expiry: {ssl_info['expiry']}\n"
        )

    else:

        output_box.insert(
            tk.END,
            "SSL Analysis Failed\n"
        )

    # Header analysis
    output_box.insert(
        tk.END,
        "\n====================================\n"
        "HEADER ANALYSIS\n"
        "====================================\n\n"
    )

    url = f"http://{target}"

    missing_headers = check_headers(url)

    if missing_headers:

        for header in missing_headers:

            output_box.insert(
                tk.END,
                f"[MISSING] {header}\n"
            )

    else:

        output_box.insert(
            tk.END,
            "No missing headers detected\n"
        )

    # Threat scoring
    output_box.insert(
        tk.END,
        "\n====================================\n"
        "THREAT SCORE\n"
        "====================================\n\n"
    )

    threat = calculate_threat_score(
        open_ports,
        risks,
        missing_headers
    )

    output_box.insert(
        tk.END,
        f"Threat Score: {threat['score']}\n"
    )

    output_box.insert(
        tk.END,
        f"Risk Level: {threat['level']}\n"
    )

    # CVE analysis
    output_box.insert(
        tk.END,
        "\n====================================\n"
        "CVE ANALYSIS\n"
        "====================================\n\n"
    )

    detected_cves = check_cves(open_ports)

    if detected_cves:

        for cve in detected_cves:

            output_box.insert(
                tk.END,
                f"{cve['cve']} "
                f"({cve['severity']})\n"
            )

            output_box.insert(
                tk.END,
                f"{cve['description']}\n\n"
            )

    else:

        output_box.insert(
            tk.END,
            "No known CVEs detected\n"
        )

    # Generate PDF report
    generate_pdf_report(
        target,
        open_ports,
        risks,
        missing_headers
    )

    output_box.insert(
        tk.END,
        "\n[+] PDF Report Generated\n"
    )

    progress.stop()

    status_label.config(
        text="Scan Completed"
    )


# Create window
app = ttk.Window(
    themename="darkly"
)

app.title(
    "Professional Security Scanner"
)

app.geometry("1200x900")

# Title
title = ttk.Label(
    app,
    text="PROFESSIONAL SECURITY SCANNER",
    font=("Arial", 22, "bold"),
    foreground="red"
)

title.pack(pady=8)

# Input frame
input_frame = ttk.Frame(app)

input_frame.pack(pady=10)

target_entry = ttk.Entry(
    input_frame,
    width=50,
    font=("Arial", 14)
)

target_entry.pack(
    side=tk.LEFT,
    padx=10
)

scan_button = ttk.Button(
    input_frame,
    text="Start Scan",
    bootstyle="danger",
    command=threaded_scan
)

scan_button.pack(
    side=tk.LEFT
)

# Progress bar
progress = Progressbar(
    app,
    mode="indeterminate",
    length=400
)

progress.pack(pady=10)

# Output box
output_box = scrolledtext.ScrolledText(
    app,
    width=120,
    height=20,
    bg="#111111",
    fg="white",
    insertbackground="white",
    font=("Consolas", 11)
)

output_box.pack(
    pady=10,
    fill="both",
    expand=True
)

# Bottom frame
bottom_frame = ttk.Frame(app)

bottom_frame.pack(pady=10)

save_button = ttk.Button(
    bottom_frame,
    text="Export Report",
    bootstyle="success",
    command=save_report
)

save_button.pack(
    side=tk.LEFT,
    padx=10
)

status_label = ttk.Label(
    bottom_frame,
    text="Ready",
    font=("Arial", 10)
)

status_label.pack(
    side=tk.LEFT
)

# Run app
app.mainloop()
