# feed_mcp.py


import os
import feedparser
from fastmcp import FastMCP
from dotenv import load_dotenv

load_dotenv()
rss_url = os.getenv("RSS_URL")
youtube_default = os.getenv("YOUTUBE_DEFAULT_URL")
youtube_channel_id = os.getenv("YOUTUBE_CHANNEL_ID")
youtube_url = youtube_default + youtube_channel_id


mcp = FastMCP("FreeCodeCamp Feed Searcher")

@mcp.tool()
def fcc_news_search(query: str, max_results: int=5) -> list:
    """
    Search the FreeCodeCamp news feed via RSS by title/description.
    """
    feed = feedparser.parse(rss_url)
    results = []
    query = query.lower()
    for entry in feed.entries[:max_results]:
        title = entry.get("title", "")
        description = entry.get("description", "")
        if query in title.lower() or query in description.lower():
            results.append({
                "Title": title,
                "Description": description,
                "Link": entry.get('link', '')})
    return results if results else [{"message" : "No results found."}]

@mcp.tool()
def fcc_youtube_search(query: str, max_results: int=5) -> list:
    """
    Search FeedCodeCamp Youtube Channel via RSS by title/description.
    """
    feed = feedparser.parse(youtube_url)
    results = []
    query = query.lower()
    for entry in feed.entries[:max_results]:
        title = entry.get("title", "")
        if query in title.lower():
            results.append({
                "Title": title,
                "Link": entry.get("link", "")
            })
    return results if results else [{"message": "No results found."}]

if __name__ == "__main__":
    mcp.run()# STDIO by default
