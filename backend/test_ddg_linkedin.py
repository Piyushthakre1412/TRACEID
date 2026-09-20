import requests
import re
import urllib.parse
import html

def test_ddg_linkedin(bio_text: str):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9'
    }

    clean_bio = bio_text.replace("|", " ").replace("\n", " ").strip()
    
    # Try Bing SERP with mobile User-Agent & bot User-Agents
    user_agents = {
        "Chrome": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "Googlebot": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
        "iPhone": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1"
    }

    query = f"site:linkedin.com/in/ {clean_bio[:60]}"
    print(f"Query: '{query}'")

    for name, ua in user_agents.items():
        h = {'User-Agent': ua, 'Accept-Language': 'en-US,en;q=0.9'}
        # Bing search
        try:
            b_url = f"https://www.bing.com/search?q={urllib.parse.quote(query)}"
            resp = requests.get(b_url, headers=h, timeout=5)
            # Find linkedin URLs
            links = re.findall(r'https?://(?:[a-z]{2,3}\.)?linkedin\.com/in/[a-zA-Z0-9_\-%]+', resp.text)
            print(f"[{name}] Bing Status: {resp.status_code}, Found LinkedIn links: {list(set(links))[:5]}")
        except Exception as e:
            print(f"[{name}] Bing Error: {e}")

if __name__ == "__main__":
    bio = "Pursuing my B tech Degree at Prof. Ram Meghe Institute of Technology & Research, Badnera. | DSA | JAVA"
    test_ddg_linkedin(bio)
