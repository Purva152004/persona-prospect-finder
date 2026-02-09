
import json
from pathlib import Path

DATA_PATH = Path("app/seed/apollo_seed.json")

def fetch_apollo_profiles(persona):
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    results = []

    title = persona.get("title", "").lower()
    location = persona.get("location", "").lower()
    industry = persona.get("industry", "").lower()

    for p in data:
        score = 0

        if title and title in p.get("title", "").lower():
            score += 1
        if location and location in p.get("location", "").lower():
            score += 1
        if industry and industry in p.get("industry", "").lower():
            score += 1

        if score >= 1:
            results.append(p)

    return results
