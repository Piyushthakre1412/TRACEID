import requests
import urllib.parse
import re

def inspect_google_html(query: str):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9'
    }

    url = f"https://www.google.com/search?q={urllib.parse.quote(query)}"
    resp = requests.get(url, headers=headers, timeout=5)
    html = resp.text
    print(f"Status: {resp.status_code}, Length: {len(html)}")

    # Search for linkedin in raw html
    linkedin_matches = re.findall(r'linkedin\.com[^\s"<>&]+', html)
    print("Raw linkedin matches:", linkedin_matches[:10])

    # Search for all hrefs
    hrefs = re.findall(r'href="([^"]+)"', html)
    l_hrefs = [h for h in hrefs if 'linkedin' in h]
    print("Href linkedin matches:", l_hrefs[:10])

if __name__ == "__main__":
    inspect_google_html('site:linkedin.com "Ram Meghe Institute"')
