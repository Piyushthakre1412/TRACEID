import requests
import urllib.parse
import re
import html

def test_bing_queries(bio_text: str):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }

    clean_bio = bio_text.replace("|", " ").replace("\n", " ").strip()

    queries = [
        'site:linkedin.com/in "Ram Meghe Institute"',
        'site:linkedin.com "Ram Meghe Institute of Technology & Research, Badnera"',
        'site:linkedin.com "Ram Meghe Institute of Technology"',
        '"Ram Meghe Institute of Technology & Research, Badnera" linkedin'
    ]

    for q in queries:
        print(f"\n--- Testing Bing Query: '{q}' ---")
        try:
            b_url = f"https://www.bing.com/search?q={urllib.parse.quote(q)}"
            resp = requests.get(b_url, headers=headers, timeout=5)
            # Extract links
            links = re.findall(r'href="(https?://(?:[a-z]{2,3}\.)?linkedin\.com/in/[^"]+)"', resp.text)
            unique_links = list(set(links))
            print("Status:", resp.status_code, "Found LinkedIn links:", unique_links[:5])

            # Extract result blocks
            blocks = re.findall(r'<li class="b_algo">(.*?)</li>', resp.text, re.DOTALL)
            print(f"Result blocks found: {len(blocks)}")
            for b in blocks[:3]:
                title = re.search(r'<h2><a [^>]*>(.*?)</a></h2>', b)
                snippet = re.search(r'<p[^>]*>(.*?)</p>', b)
                link = re.search(r'href="(https?://[^"]+)"', b)
                t_str = re.sub(r'<[^>]+>', '', title.group(1)) if title else "None"
                s_str = re.sub(r'<[^>]+>', '', snippet.group(1)) if snippet else "None"
                l_str = link.group(1) if link else "None"
                print("  Title:", t_str)
                print("  Link:", l_str)
                print("  Snippet:", s_str[:100])
                print("-" * 30)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    bio = "Pursuing my B tech Degree at Prof. Ram Meghe Institute of Technology & Research, Badnera. | DSA | JAVA"
    test_bing_queries(bio)
