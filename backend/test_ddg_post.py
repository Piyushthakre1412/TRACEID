import requests
import urllib.parse
import re
import html

def test_ddg_post(query: str):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    url = "https://html.duckduckgo.com/html/"
    resp = requests.post(url, data={'q': query}, headers=headers, timeout=5)
    print(f"Status: {resp.status_code}, Length: {len(resp.text)}")

    # Extract all result links & titles from DDG HTML
    # DDG HTML result items are in <div class="result result--default ...">
    # Links are wrapped in uddg=https%3A%2F%2Fin.linkedin.com%2Fin%2F...
    raw_uddg = re.findall(r'uddg=([^&"\']+)', resp.text)
    decoded_links = [urllib.parse.unquote(l) for l in raw_uddg]
    linkedin_links = [l for l in decoded_links if 'linkedin.com/in/' in l]

    print(f"Discovered {len(linkedin_links)} LinkedIn profile URLs:")
    for l in list(set(linkedin_links))[:5]:
        print(" ", l)

    # Extract titles and snippets
    # DDG titles: <a class="result__a" href="...">Title</a>
    # DDG snippets: <a class="result__snippet" ...>Snippet</a>
    titles = re.findall(r'<a class="result__a"[^>]*>(.*?)</a>', resp.text, re.DOTALL)
    snippets = re.findall(r'<a class="result__snippet"[^>]*>(.*?)</a>', resp.text, re.DOTALL)

    print(f"Discovered {len(titles)} result titles:")
    for t in titles[:5]:
        print("  -", re.sub(r'<[^>]+>', '', html.unescape(t)).strip())

if __name__ == "__main__":
    test_ddg_post('site:linkedin.com "Ram Meghe Institute"')
    test_ddg_post('site:linkedin.com "Ram Meghe Institute" "DSA"')
