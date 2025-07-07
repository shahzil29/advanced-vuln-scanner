import nmap

def scan_target(ip):
    scanner = nmap.PortScanner()
    print(f"[+] Scanning {ip}...")
    scanner.scan(ip, arguments='-sV')
    
    results = []
    for host in scanner.all_hosts():
        for proto in scanner[host].all_protocols():
            for port in scanner[host][proto].keys():
                service = scanner[host][proto][port]
                results.append({
                    'port': port,
                    'name': service['name'],
                    'product': service.get('product', ''),
                    'version': service.get('version', '')
                })
    return results
