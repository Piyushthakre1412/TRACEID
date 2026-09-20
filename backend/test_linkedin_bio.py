import requests
import urllib.parse
import re

def test_web_search_bio(bio_text: str):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    clean_bio = bio_text.replace("|", " ").replace("\n", " ").strip()
    
    # 1. Search Google HTML SERP
    print("--- Searching Google HTML SERP ---")
    g_url = f"https://www.google.com/search?q={urllib.parse.quote(clean_bio)}"
    try:
        resp = requests.get(g_url, headers=headers, timeout=5)
        print("Google Status:", resp.status_code)
        # Find LinkedIn URLs in google HTML
        linkedin_urls = re.findall(r'https?://(?:www\.)?linkedin\.com/in/[a-zA-Z0-9_\-%]+', resp.text)
        print("Google found LinkedIn URLs:", list(set(linkedin_urls)))

        # Find all result snippets in google HTML
        # Result titles in Google HTML: <h3>...</h3>
        titles = re.findall(r'<h3[^>]*>(.*?)</h3>', resp.text)
        print("Google Result Titles:", [re.sub(r'<[^>]+>', '', t) for t in titles[:5]])
    except Exception as e:
        print("Google search error:", e)

    # 2. Search Bing HTML SERP
    print("\n--- Searching Bing HTML SERP ---")
    b_url = f"https://www.bing.com/search?q={urllib.parse.quote(clean_bio)}"
    try:
        resp = requests.get(b_url, headers=headers, timeout=5)
        print("Bing Status:", resp.status_code)
        b_linkedin = re.findall(r'https?://(?:www\.)?linkedin\.com/in/[a-zA-Z0-9_\-%]+', resp.text)
        print("Bing found LinkedIn URLs:", list(set(b_linkedin)))
    except Exception as e:
        print("Bing search error:", e)

if __name__ == "__main__":
    bio = "Pursuing my B tech Degree at Prof. Ram Meghe Institute of Technology & Research, Badnera. | DSA | JAVA"
    test_web_search_bio(bio)
