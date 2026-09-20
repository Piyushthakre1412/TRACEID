import requests
import urllib.parse
import re
import html

def test_yahoo(query: str):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9'
    }

    url = f"https://search.yahoo.com/search?p={urllib.parse.quote(query)}"
    print(f"Testing Yahoo: '{query}'")
    resp = requests.get(url, headers=headers, timeout=5)
    print("Status:", resp.status_code, "Length:", len(resp.text))

    # Extract LinkedIn links from Yahoo HTML
    links = re.findall(r'href="([^"]+)"', resp.text)
    linkedin_links = []
    for l in links:
        unquoted = urllib.parse.unquote(l)
        if "linkedin.com/in/" in unquoted:
            # Extract actual URL if inside Yahoo redirect
            m = re.search(r'(https?://[^\s"/]*linkedin\.com/in/[^\s"/&]+)', unquoted)
            if m:
                linkedin_links.append(m.group(1))

    print(f"Yahoo discovered {len(linkedin_links)} LinkedIn URLs:")
    for l in list(set(linkedin_links))[:5]:
        print(" ", l)

    # Extract titles and snippets
    # In Yahoo, titles: <h3 class="title"><a ...>Title</a></h3>
    titles = re.findall(r'<h3 class="title"[^>]*>(.*?)</h3>', resp.text, re.DOTALL)
    snippets = re.findall(r'<div class="compText[^"]*"[^>]*>(.*?)</div>', resp.text, re.DOTALL)

    print(f"Discovered {len(titles)} Yahoo titles:")
    for t in titles[:5]:
        print("  -", re.sub(r'<[^>]+>', '', html.unescape(t)).strip())

if __name__ == "__main__":
    bio = "Pursuing my B tech Degree at Prof. Ram Meghe Institute of Technology & Research, Badnera"
    test_yahoo(f'site:linkedin.com/in/ "{bio}"')
    test_yahoo(f'site:linkedin.com/in/ {bio}')
