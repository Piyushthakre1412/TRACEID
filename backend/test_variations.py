import requests
import urllib.parse
import re
import html

def test_query_variations(bio_text: str):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9'
    }

    clean_bio = bio_text.replace("|", " ").replace("\n", " ").strip()
    
    variations = [
        f'site:linkedin.com/in/ "{clean_bio[:40]}"',
        f'site:linkedin.com/in/ {clean_bio}',
        f'site:linkedin.com "Ram Meghe Institute of Technology & Research" "DSA" "JAVA"',
        f'site:linkedin.com/in/ "Ram Meghe Institute"'
    ]

    for q in variations:
        print(f"\n--- Testing Query: '{q}' ---")
        try:
            g_url = f"https://www.google.com/search?q={urllib.parse.quote(q)}"
            resp = requests.get(g_url, headers=headers, timeout=5)
            print("Google Status:", resp.status_code)
            
            # Extract links
            links = re.findall(r'https?://(?:[a-z]{2,3}\.)?linkedin\.com/in/[a-zA-Z0-9_\-%]+', resp.text)
            unique_links = list(set(links))
            print("Found LinkedIn links:", unique_links[:5])

            # Extract titles
            titles = re.findall(r'<h3[^>]*>(.*?)</h3>', resp.text)
            clean_titles = [re.sub(r'<[^>]+>', '', t) for t in titles if 'LinkedIn' in t or 'Prof' in t or 'Student' in t or 'B' in t or 'Ram' in t]
            print("Found Titles:", clean_titles[:5])
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    bio = "Pursuing my B tech Degree at Prof. Ram Meghe Institute of Technology & Research, Badnera. | DSA | JAVA"
    test_query_variations(bio)
