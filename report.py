from fpdf import FPDF

def generate_report(ip, results):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Scan Report for {ip}", ln=True)

    for result in results:
        pdf.cell(200, 10, txt=f"Port: {result['port']}", ln=True)
        pdf.cell(200, 10, txt=f"Service: {result['name']} {result['product']} {result['version']}", ln=True)
        pdf.cell(200, 10, txt="CVEs:", ln=True)
        for cve in result['cves']:
            pdf.cell(200, 10, txt=f" - {cve}", ln=True)

    pdf.output(f"{ip}_report.pdf")
