import requests
import urllib.parse
import re

from app.config import settings

def test_google_custom(context: str):
    api_key = settings.GOOGLE_SEARCH_API_KEY
    cx = settings.GOOGLE_SEARCH_ENGINE_ID
    print(f"API Key present: {bool(api_key)}, CX: {cx}")

    clean_context = context.replace("|", " ").strip()
    
    # 1. Google Custom Search query
    queries = [
        clean_context,
        f"site:linkedin.com {clean_context}"
    ]

    for q in queries:
        print(f"\n--- Querying Custom Search: '{q[:60]}...' ---")
        if api_key and cx:
            url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={urllib.parse.quote(q)}"
            resp = requests.get(url, timeout=5)
            print("Status:", resp.status_code)
            if resp.status_code == 200:
                data = resp.json()
                items = data.get("items", [])
                print(f"Found {len(items)} items:")
                for item in items[:5]:
                    print("  Title:", item.get("title"))
                    print("  Link:", item.get("link"))
                    print("  Snippet:", item.get("snippet"))
                    print("-" * 30)

if __name__ == "__main__":
    bio = "Pursuing my B tech Degree at Prof. Ram Meghe Institute of Technology & Research, Badnera. | DSA | JAVA"
    test_google_custom(bio)
