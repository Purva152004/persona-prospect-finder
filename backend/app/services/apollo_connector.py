import json
from pathlib import Path

DATA_PATH = Path("app/seed/apollo_seed.json")

def fetch_apollo_profiles(persona):
    with open(DATA_PATH) as f:
        data = json.load(f)

    results = []

    for p in data:
        if persona["title"] in p["title"].lower() and \
           persona["location"] in p["location"].lower() and \
           persona["industry"] in p["industry"].lower():
            results.append(p)

    return results
