from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf_report(
    target,
    open_ports,
    risks,
    missing_headers
):

    doc = SimpleDocTemplate("security_report.pdf")

    styles = getSampleStyleSheet()

    elements = []

    # Title
    elements.append(
        Paragraph(
            "Professional Security Scan Report",
            styles['Title']
        )
    )

    elements.append(Spacer(1, 20))

    # Target
    elements.append(
        Paragraph(
            f"<b>Target:</b> {target}",
            styles['BodyText']
        )
    )

    elements.append(Spacer(1, 15))

    # Open ports
    elements.append(
        Paragraph(
            "<b>Open Ports & Services</b>",
            styles['Heading2']
        )
    )

    for item in open_ports:

        elements.append(
            Paragraph(
                f"Port {item['port']} "
                f"→ {item['banner']}",
                styles['BodyText']
            )
        )

    elements.append(Spacer(1, 15))

    # Risks
    elements.append(
        Paragraph(
            "<b>Risk Analysis</b>",
            styles['Heading2']
        )
    )

    if risks:

        for risk in risks:

            elements.append(
                Paragraph(
                    f"HIGH RISK → "
                    f"Port {risk['port']} : "
                    f"{risk['risk']}",
                    styles['BodyText']
                )
            )

    else:

        elements.append(
            Paragraph(
                "No major risks detected",
                styles['BodyText']
            )
        )

    elements.append(Spacer(1, 15))

    # Missing headers
    elements.append(
        Paragraph(
            "<b>Missing Security Headers</b>",
            styles['Heading2']
        )
    )

    if missing_headers:

        for header in missing_headers:

            elements.append(
                Paragraph(
                    header,
                    styles['BodyText']
                )
            )

    else:

        elements.append(
            Paragraph(
                "No missing headers",
                styles['BodyText']
            )
        )

    # Generate PDF
    doc.build(elements)

    print("\n[+] PDF Report Generated")
