import requests
import urllib.parse
import re
import html
from typing import List, Dict, Any

def search_open_web_profiles(query: str, context: str = "") -> List[Dict[str, Any]]:
    """
    Open Web Profile Recon Search Engine.
    Queries public web search endpoints for LinkedIn, Instagram, GitHub, X social media profiles using name & bio context.
    """
    results = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9'
    }

    clean_q = query.strip()
    clean_ctx = context.replace("|", " ").replace("\n", " ").strip()
    full_text = f"{clean_q} {clean_ctx}".strip()

    if not full_text:
        return results

    # Construct targeted search queries for LinkedIn, Instagram, GitHub
    search_queries = []
    if clean_q:
        search_queries.append(f'"{clean_q}" {clean_ctx}')
        search_queries.append(f'site:linkedin.com/in/ "{clean_q}"')
    else:
        # Bio-only search: extract main keywords or bio snippet
        snippet = clean_ctx[:80]
        search_queries.append(f'site:linkedin.com/in/ {snippet}')
        search_queries.append(f'site:instagram.com {snippet}')
        search_queries.append(clean_ctx)

    for q in search_queries:
        try:
            # Query Bing Search API / HTML endpoint
            b_url = f"https://www.bing.com/search?q={urllib.parse.quote(q)}"
            resp = requests.get(b_url, headers=headers, timeout=4)
            if resp.status_code == 200:
                raw_html = resp.text
                
                # Extract result blocks (li class="b_algo")
                blocks = re.findall(r'<li class="b_algo">(.*?)</li>', raw_html, re.DOTALL)
                for b in blocks:
                    link_match = re.search(r'href="(https?://[^"]+)"', b)
                    title_match = re.search(r'<h2><a [^>]*>(.*?)</a></h2>', b)
                    snippet_match = re.search(r'<p[^>]*>(.*?)</p>', b)

                    if link_match:
                        link = link_match.group(1)
                        if "bing.com" in link or "microsoft.com" in link:
                            continue

                        raw_title = re.sub(r'<[^>]+>', '', title_match.group(1)) if title_match else ""
                        raw_snippet = re.sub(r'<[^>]+>', '', snippet_match.group(1)) if snippet_match else ""

                        clean_title = html.unescape(raw_title).strip()
                        clean_snippet = html.unescape(raw_snippet).strip()

                        # Determine platform
                        platform = "Open Web Profile"
                        if "linkedin.com" in link:
                            platform = "LinkedIn"
                        elif "instagram.com" in link:
                            platform = "Instagram"
                        elif "github.com" in link:
                            platform = "GitHub"
                        elif "twitter.com" in link or "x.com" in link:
                            platform = "X (Twitter)"
                        elif "dev.to" in link:
                            platform = "Dev.to"
                        elif "medium.com" in link:
                            platform = "Medium"

                        # Extract username & canonical name
                        username = clean_q or "target"
                        if "/in/" in link:
                            username = link.split("/in/")[-1].split("/")[0].split("?")[0]
                        elif "instagram.com/" in link:
                            username = link.split("instagram.com/")[-1].split("/")[0].split("?")[0]
                        elif "github.com/" in link:
                            username = link.split("github.com/")[-1].split("/")[0].split("?")[0]

                        # Clean canonical name from title
                        # e.g. "John Doe - Student - Ram Meghe Institute | LinkedIn" -> "John Doe"
                        canonical_name = clean_title.split("-")[0].split("|")[0].split("–")[0].split("•")[0].strip()
                        if not canonical_name or len(canonical_name) < 2 or "LinkedIn" in canonical_name or "Instagram" in canonical_name:
                            canonical_name = clean_q.title() if clean_q else "Discovered Target Profile"

                        results.append({
                            "platform": platform,
                            "username": username,
                            "canonical_name": canonical_name,
                            "bio": clean_snippet or clean_ctx,
                            "avatar_url": None,
                            "profile_url": link,
                            "institution": f"{platform} Profile"
                        })
        except Exception as e:
            print(f"Open Web Search Warning for query '{q}': {e}")

    # Deduplicate by profile_url
    seen_urls = set()
    final_results = []
    for r in results:
        if r["profile_url"] not in seen_urls:
            seen_urls.add(r["profile_url"])
            final_results.append(r)

    return final_results

if __name__ == "__main__":
    bio = "Pursuing my B tech Degree at Prof. Ram Meghe Institute of Technology & Research, Badnera. | DSA | JAVA"
    res = search_open_web_profiles("", bio)
    print(f"Discovered {len(res)} open web profiles:")
    for r in res:
        print(f" [{r['platform']}] {r['canonical_name']} (@{r['username']})")
        print(f"   URL: {r['profile_url']}")
        print(f"   Bio: {r['bio'][:100]}")
        print("-" * 50)
