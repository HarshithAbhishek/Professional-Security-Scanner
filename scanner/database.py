import sqlite3
from datetime import datetime

# Create database connection
conn = sqlite3.connect("scanner.db")

cursor = conn.cursor()

# Create scans table
cursor.execute("""

CREATE TABLE IF NOT EXISTS scans (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    target TEXT,

    open_ports TEXT,

    risks TEXT,

    scan_time TEXT

)

""")

conn.commit()


# Save scan results
def save_scan(target, open_ports, risks):

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    ports_text = ", ".join(
        [str(item['port']) for item in open_ports]
    )

    risks_text = ", ".join(
        [risk['risk'] for risk in risks]
    )

    cursor.execute("""

    INSERT INTO scans (
        target,
        open_ports,
        risks,
        scan_time
    )

    VALUES (?, ?, ?, ?)

    """, (
        target,
        ports_text,
        risks_text,
        timestamp
    ))

    conn.commit()

    print("[+] Scan saved to database")
