import requests
import urllib.parse
import re

def test_unquoted(bio_text: str):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }

    unquoted_queries = [
        "site:linkedin.com/in/ Ram Meghe Institute Badnera",
        "site:linkedin.com/in/ Ram Meghe Institute",
        "site:linkedin.com Ram Meghe Institute Badnera DSA JAVA",
        "site:linkedin.com/in/ Piyush Thakre Ram Meghe"
    ]

    for q in unquoted_queries:
        print(f"\n--- Testing Bing Query: '{q}' ---")
        try:
            url = f"https://www.bing.com/search?q={urllib.parse.quote(q)}"
            resp = requests.get(url, headers=headers, timeout=5)
            print("Status:", resp.status_code)
            links = re.findall(r'href="(https?://(?:[a-z]{2,3}\.)?linkedin\.com/in/[^"]+)"', resp.text)
            print("Found LinkedIn URLs:", list(set(links))[:5])

            titles = re.findall(r'<h2><a [^>]*>(.*?)</a></h2>', resp.text)
            clean_t = [re.sub(r'<[^>]+>', '', t) for t in titles]
            print("Found Titles:", clean_t[:5])
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    bio = "Pursuing my B tech Degree at Prof. Ram Meghe Institute of Technology & Research, Badnera. | DSA | JAVA"
    test_unquoted(bio)
