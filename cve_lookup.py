import requests

def get_cves(service, version):
    try:
        query = f"{service} {version}"
        url = f"https://cve.circl.lu/api/search/{query}"
        r = requests.get(url)
        data = r.json()
        cves = [item['id'] for item in data.get('data', [])][:5]
        return cves
    except:
        return ["No CVEs found"]
