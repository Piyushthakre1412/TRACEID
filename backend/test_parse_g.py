import requests
import urllib.parse
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9'
}

query = 'site:linkedin.com "Ram Meghe Institute"'
url = f"https://www.google.com/search?q={urllib.parse.quote(query)}"
resp = requests.get(url, headers=headers, timeout=5)
print("Status:", resp.status_code, "Length:", len(resp.text))

with open("scratch_g.html", "w", encoding="utf-8") as f:
    f.write(resp.text)

# Inspect all URLs containing linkedin or http in scratch_g.html
urls = re.findall(r'href="([^"]+)"', resp.text)
l_urls = [u for u in urls if 'linkedin' in u or 'http' in u]
print(f"Total hrefs: {len(urls)}, Sample hrefs:", l_urls[:10])
