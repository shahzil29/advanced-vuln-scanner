from scanner import scan_target
from cve_lookup import get_cves
from report import generate_report
from rich.table import Table
from rich.console import Console

console = Console()

def display(results):
    table = Table(title="Scan Results")
    table.add_column("Port", style="cyan")
    table.add_column("Service")
    table.add_column("Version")
    table.add_column("Top CVE")

    for res in results:
        cve = res['cves'][0] if res['cves'] else "None"
        table.add_row(str(res['port']), res['name'], res['version'], cve)

    console.print(table)

if __name__ == "__main__":
    ip = input("Enter Target IP: ")
    data = scan_target(ip)

    for d in data:
        d['cves'] = get_cves(d['name'], d['version'])

    display(data)
    generate_report(ip, data)
