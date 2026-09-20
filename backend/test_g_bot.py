import requests
import urllib.parse
import re
import html

def test_g_bot(query: str):
    user_agents = {
        "Googlebot": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
        "Facebookbot": "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)",
        "Twitterbot": "Twitterbot/1.0",
        "Chrome": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }

    clean_q = query.replace("|", " ").strip()
    
    for name, ua in user_agents.items():
        print(f"\n--- Testing Google with [{name}] ---")
        headers = {'User-Agent': ua, 'Accept-Language': 'en-US,en;q=0.9'}
        url = f"https://www.google.com/search?q={urllib.parse.quote(clean_q)}"
        try:
            resp = requests.get(url, headers=headers, timeout=5)
            print(f"[{name}] Status: {resp.status_code}, Length: {len(resp.text)}")
            
            # Find LinkedIn URLs in Google HTML
            links = re.findall(r'https?://(?:[a-z]{2,3}\.)?linkedin\.com/in/[a-zA-Z0-9_\-%]+', resp.text)
            unique_links = list(set(links))
            print(f"[{name}] Discovered LinkedIn URLs: {unique_links[:5]}")
            
            # Find Titles
            titles = re.findall(r'<h3[^>]*>(.*?)</h3>', resp.text)
            clean_titles = [re.sub(r'<[^>]+>', '', t) for t in titles]
            print(f"[{name}] Discovered Titles: {clean_titles[:5]}")
        except Exception as e:
            print(f"[{name}] Error: {e}")

if __name__ == "__main__":
    test_g_bot('site:linkedin.com/in/ "Ram Meghe Institute"')
    test_g_bot('site:linkedin.com/in/ Ram Meghe Institute Badnera DSA JAVA')
