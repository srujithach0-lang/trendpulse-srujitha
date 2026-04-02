import requests
import json
import os
import time
from datetime import datetime

# --- constants & configuration ---
TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL_TEMPLATE = "https://hacker-news.firebaseio.com/v0/item/{id}.json"
# mandatory Headers
headers = {"User-Agent": "TrendPulse/1.0"}
DATA_DIR = "data"
# Mapping categories to keywords for matching
CATEGORIES ={
    "technology": ["ai", "software", "tech", "code", "data", "cloud", "API", "GPU", "LLM"],
    "worldnews": ["war", "government", "country", "president", "election","climate", "attack", "global"],
    "sports": ["NFL", 'NBA', "FIFA", "sport", "game", "team", "player", "league", "championship", "hockey", "tennis", "golf"],
    "science":["research", "study", "space", "physics", "biology", "discovery", "NASA", "genome", "AI in science", "datascience", "environment"],
    "entertainment":["movies", "film", "music", "Netflix", "game", "book", "show", "award", "streaming", "celebrity", "tv", "anime"]

}
def task_1_fetch():
    # 1. Create data folder if it doesn't exist
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    print("Fetching ID's...")
    ids = requests.get(TOP_STORIES_URL, headers = headers).json()[:500]
    all_stories = []

    for cat_name, keywords in CATEGORIES.items():
        #stop if already hit 25 stories for this category
        found = 0
        for s_id in ids:
            if found >= 25: 
                break
            try:
                story = requests.get(ITEM_URL_TEMPLATE.format(id=s_id), headers = headers).json()
                title = story.get('title', '')
                # Case-insensitive check: if any keyword exist in the title
                if any(word.lower() in title.lower() for word in keywords):
                    # Extract the 7 reruried fields
                    all_stories.append({
                        "post_id": story.get("id"),
                        "title": title,
                        "category": cat_name,
                        "score": story.get("score", 0),
                        "num_comments": story.get("descendants", 0),
                        "author": story.get("by", "unknown"),
                        "collected_at": datetime.now().strftime("%y-%m-%d %H:%M:%S")

                    })
            
                    found += 1
            except: continue
        print(f"Finished {cat_name} with {found} stories")
        # Requried: 2s delay between requests to avoid hitting API limits
        time.sleep(2)

    # save to json file
    filename = f"{DATA_DIR}/trends_{datetime.now().strftime('%Y%m%d')}.json"
    with open(filename, 'w') as f:
        json.dump(all_stories, f, indent=4)
    print(f"collected {len(all_stories)} stories. Saved to {filename}")
    return filename

if __name__ == "__main__":
    json_file = task_1_fetch()