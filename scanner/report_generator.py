from datetime import datetime

def generate_html_report(
    target,
    open_ports,
    risks,
    missing_headers
):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    html_content = f"""
<!DOCTYPE html>

<html>

<head>

<title>Security Scan Report</title>

<style>

body {{

    background-color: #0f1117;
    color: #ffffff;
    font-family: Arial, sans-serif;
    padding: 30px;
}}

h1 {{

    color: #ff4d4d;
    text-align: center;
}}

.section {{

    background-color: #1a1d26;
    padding: 20px;
    margin-bottom: 25px;
    border-radius: 12px;
    box-shadow: 0px 0px 10px rgba(0,0,0,0.5);
}}

.section h2 {{

    color: #00d4ff;
}}

.card {{

    background-color: #2a2f3a;
    padding: 12px;
    margin-top: 10px;
    border-radius: 8px;
}}

.high-risk {{

    color: #ff4d4d;
    font-weight: bold;
}}

.safe {{

    color: #00ff99;
}}

</style>

</head>

<body>

<h1>PROFESSIONAL SECURITY SCAN REPORT</h1>

<div class="section">

<h2>Target Information</h2>

<div class="card">
<p><b>Target:</b> {target}</p>
<p><b>Scan Time:</b> {timestamp}</p>
</div>

</div>

<div class="section">

<h2>Open Ports & Services</h2>
"""

    for item in open_ports:

        html_content += f"""
<div class="card">

<p>
<b>Port:</b> {item['port']}
</p>

<p>
<b>Service:</b> {item['banner']}
</p>

</div>
"""

    html_content += """
</div>

<div class="section">

<h2>Risk Analysis</h2>
"""

    if risks:

        for risk in risks:

            html_content += f"""
<div class="card">

<p class="high-risk">
HIGH RISK
</p>

<p>
<b>Port:</b> {risk['port']}
</p>

<p>
{risk['risk']}
</p>

</div>
"""

    else:

        html_content += """
<div class="card">

<p class="safe">
No major risks detected
</p>

</div>
"""

    html_content += """
</div>

<div class="section">

<h2>Missing Security Headers</h2>
"""

    if missing_headers:

        for header in missing_headers:

            html_content += f"""
<div class="card">

<p>{header}</p>

</div>
"""

    else:

        html_content += """
<div class="card">

<p class="safe">
No missing security headers
</p>

</div>
"""

    html_content += """
</div>

</body>
</html>
"""

    with open("report.html", "w") as file:

        file.write(html_content)

    print("\n[+] Professional HTML Report Generated")
