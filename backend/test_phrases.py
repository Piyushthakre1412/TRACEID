import requests
import urllib.parse
import re
import html

def extract_bio_search_phrases(bio_text: str):
    clean_bio = bio_text.replace("|", " ").replace("\n", " ").strip()
    phrases = []
    
    # 1. Look for institution/org patterns: e.g. "Prof. Ram Meghe Institute of Technology & Research"
    org_matches = re.findall(r'((?:[A-Z][a-zA-Z0-9&\.]+\s+){2,}(?:Institute|University|College|School|Technology|Research|Corporation|Inc|Ltd|Company|Lab)[a-zA-Z0-9&\.\,\s]*)', bio_text)
    for om in org_matches:
        phrases.append(om.strip().strip(",").strip("."))
        
    # 2. Split by punctuation / bars
    parts = [p.strip() for p in re.split(r'[\|\.\n\•]', bio_text) if len(p.strip()) > 8]
    phrases.extend(parts[:3])

    print("Extracted Bio Search Phrases:", phrases)
    return phrases

def test_phrase_searches(bio_text: str):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }
    phrases = extract_bio_search_phrases(bio_text)

    for p in phrases[:3]:
        q = f'site:linkedin.com/in/ "{p}"'
        print(f"\n--- Testing Bing Query: '{q}' ---")
        try:
            url = f"https://www.bing.com/search?q={urllib.parse.quote(q)}"
            resp = requests.get(url, headers=headers, timeout=5)
            print("Status:", resp.status_code)
            
            # Extract links
            links = re.findall(r'href="(https?://(?:[a-z]{2,3}\.)?linkedin\.com/in/[^"]+)"', resp.text)
            print("Found LinkedIn URLs:", list(set(links))[:5])

            # Extract titles
            titles = re.findall(r'<h2><a [^>]*>(.*?)</a></h2>', resp.text)
            clean_t = [re.sub(r'<[^>]+>', '', t) for t in titles]
            print("Found Titles:", clean_t[:5])
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    bio = "Pursuing my B tech Degree at Prof. Ram Meghe Institute of Technology & Research, Badnera. | DSA | JAVA"
    test_phrase_searches(bio)
