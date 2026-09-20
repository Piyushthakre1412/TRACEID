import requests
import re
import urllib.parse
import html

def search_linkedin_by_bio(bio_text: str):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9'
    }

    clean_bio = bio_text.replace("|", " ").replace("\n", " ").strip()
    # Extract key phrases: e.g. "Ram Meghe Institute of Technology"
    keywords = [w for w in clean_bio.split() if len(w) > 3][:8]
    kw_query = " ".join(keywords)

    print(f"Keywords query: '{kw_query}'")

    results = []

    # Strategy 1: Google SERP Scraping for LinkedIn Profiles
    try:
        g_url = f"https://www.google.com/search?q={urllib.parse.quote('site:linkedin.com/in/ ' + kw_query)}"
        resp = requests.get(g_url, headers=headers, timeout=5)
        print("Google SERP Status:", resp.status_code)
        
        # Extract LinkedIn profile URLs and titles from Google HTML
        # In Google HTML, links are href="/url?q=https://www.linkedin.com/in/username..." or href="https://www.linkedin.com/in/..."
        matches = re.findall(r'href="(?:/url\?q=)?(https?://(?:[a-z]{2,3}\.)?linkedin\.com/in/[a-zA-Z0-9_\-%]+)[&"]', resp.text)
        print("Discovered LinkedIn URLs from Google:", list(set(matches)))

        # Extract title and snippet blocks from Google HTML
        blocks = re.findall(r'<div class="g">(.*?)</div></div></div>', resp.text, re.DOTALL)
        for b in blocks:
            link_match = re.search(r'href="(?:/url\?q=)?(https?://(?:[a-z]{2,3}\.)?linkedin\.com/in/[a-zA-Z0-9_\-%]+)', b)
            title_match = re.search(r'<h3[^>]*>(.*?)</h3>', b)
            snippet_match = re.search(r'<div[^>]*class="[^"]*VwiC3d[^"]*"[^>]*>(.*?)</div>', b) or re.search(r'<span[^>]*>(.*?)</span>', b)
            
            if link_match:
                l = link_match.group(1)
                t = re.sub(r'<[^>]+>', '', title_match.group(1)) if title_match else "LinkedIn Member"
                s = re.sub(r'<[^>]+>', '', snippet_match.group(1)) if snippet_match else clean_bio
                
                # Title clean: e.g. "Piyush Thakre - Student - Ram Meghe Institute | LinkedIn" -> "Piyush Thakre"
                name_clean = t.split("-")[0].split("|")[0].split("–")[0].strip()
                
                results.append({
                    "platform": "LinkedIn",
                    "username": l.split("/in/")[-1].strip("/"),
                    "canonical_name": html.unescape(name_clean),
                    "bio": html.unescape(s),
                    "avatar_url": None,
                    "profile_url": l,
                    "institution": "LinkedIn Professional Profile"
                })
    except Exception as e:
        print("Google SERP Error:", e)

    # Strategy 2: Bing SERP Scraping for LinkedIn Profiles
    if not results:
        try:
            b_url = f"https://www.bing.com/search?q={urllib.parse.quote('site:linkedin.com/in/ ' + kw_query)}"
            resp = requests.get(b_url, headers=headers, timeout=5)
            print("Bing SERP Status:", resp.status_code)
            
            b_blocks = re.findall(r'<li class="b_algo">(.*?)</li>', resp.text, re.DOTALL)
            for b in b_blocks:
                link_match = re.search(r'href="(https?://(?:[a-z]{2,3}\.)?linkedin\.com/in/[^"]+)"', b)
                title_match = re.search(r'<h2><a [^>]*>(.*?)</a></h2>', b)
                snippet_match = re.search(r'<p[^>]*>(.*?)</p>', b)
                
                if link_match:
                    l = link_match.group(1)
                    t = re.sub(r'<[^>]+>', '', title_match.group(1)) if title_match else "LinkedIn Member"
                    s = re.sub(r'<[^>]+>', '', snippet_match.group(1)) if snippet_match else clean_bio
                    name_clean = t.split("-")[0].split("|")[0].split("–")[0].strip()
                    
                    results.append({
                        "platform": "LinkedIn",
                        "username": l.split("/in/")[-1].strip("/"),
                        "canonical_name": html.unescape(name_clean),
                        "bio": html.unescape(s),
                        "avatar_url": None,
                        "profile_url": l,
                        "institution": "LinkedIn Professional Profile"
                    })
        except Exception as e:
            print("Bing SERP Error:", e)

    print(f"\nTotal LinkedIn results discovered: {len(results)}")
    for r in results:
        print(" Canonical Name:", r['canonical_name'])
        print(" Username:", r['username'])
        print(" Profile URL:", r['profile_url'])
        print(" Bio:", r['bio'][:100])
        print("-" * 40)
        
    return results

if __name__ == "__main__":
    bio = "Pursuing my B tech Degree at Prof. Ram Meghe Institute of Technology & Research, Badnera. | DSA | JAVA"
    search_linkedin_by_bio(bio)
