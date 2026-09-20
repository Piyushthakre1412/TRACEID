import requests
import urllib.parse
import re
import html

def test_ddg_get(bio_text: str):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9'
    }

    clean_bio = bio_text.replace("|", " ").replace("\n", " ").strip()
    q = f"site:linkedin.com {clean_bio[:50]}"
    url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(q)}"

    print(f"Testing DDG GET: '{q}'")
    resp = requests.get(url, headers=headers, timeout=5)
    print("Status:", resp.status_code, "Length:", len(resp.text))

    # Extract links from DDG HTML (l/?uddg=...)
    links = re.findall(r'uddg=([^&"\']+)', resp.text)
    decoded_links = [urllib.parse.unquote(l) for l in links if 'linkedin.com/in' in urllib.parse.unquote(l)]
    print(f"Found {len(decoded_links)} LinkedIn profile URLs:")
    for l in list(set(decoded_links))[:5]:
        print(" ", l)

if __name__ == "__main__":
    bio = "Pursuing my B tech Degree at Prof. Ram Meghe Institute of Technology & Research, Badnera. | DSA | JAVA"
    test_ddg_get(bio)
