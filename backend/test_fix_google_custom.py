import requests
import urllib.parse
import html
import re

from app.config import settings
from app.services.text_engine import text_engine

def test_google_custom_bio_only(context: str):
    api_key = settings.GOOGLE_SEARCH_API_KEY
    cx = settings.GOOGLE_SEARCH_ENGINE_ID
    print(f"Testing with API Key: '{api_key[:10]}...', CX: '{cx}'")

    clean_context = context.replace("|", " ").strip()
    
    # Clean query string
    full_q = clean_context
    url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={urllib.parse.quote(full_q)}"
    
    print(f"Requesting URL: {url[:80]}...")
    try:
        resp = requests.get(url, timeout=5)
        print("Status code:", resp.status_code)
        if resp.status_code == 200:
            data = resp.json()
            items = data.get("items", [])
            print(f"Discovered {len(items)} items from Google Custom Search:")
            for item in items:
                title = item.get("title", "")
                link = item.get("link", "")
                snippet = item.get("snippet", "")
                print("  Title:", title)
                print("  Link:", link)
                print("  Snippet:", snippet)
                print("  Bio Similarity to Context:", text_engine.get_bio_similarity(snippet, clean_context))
                print("-" * 40)
        else:
            print("Response error body:", resp.text)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    bio = "Pursuing my B tech Degree at Prof. Ram Meghe Institute of Technology & Research, Badnera. | DSA | JAVA"
    test_google_custom_bio_only(bio)
