from fastapi import APIRouter
from app.schemas import PersonaInput
from app.services.persona_normalizer import normalize
from app.services.apollo_connector import fetch_apollo_profiles
from app.services.scorer import score_profile
from app.services.deduplicator import deduplicate
from app.services.sheets_exporter import export_to_sheets

router = APIRouter()

@router.post("/prospects")
def get_prospects(persona: PersonaInput):
    normalized = normalize(persona)
    profiles = fetch_apollo_profiles(normalized)

    output = []

    for p in profiles:
        score, reason = score_profile(p, normalized)
        output.append({
            **p,
            "email": p["email"] or "not available",
            "phone": p["phone"] or "not available",
            "score": score,
            "reason": reason,
            "source": "Apollo (Seeded)"
        })

    output = deduplicate(output)
    output.sort(key=lambda x: x["score"], reverse=True)

    sheet_rows = [
        [
            o["first_name"], o["last_name"], o["title"], o["company"],
            o["location"], o["industry"], o["experience"],
            o["profile_url"], o["email"], o["phone"],
            o["score"], o["source"]
        ] for o in output
    ]

    #export_to_sheets(sheet_rows)
    return output
