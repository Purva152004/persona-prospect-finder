from fastapi import APIRouter
from app.schemas import PersonaInput
from app.services.persona_normalizer import normalize
from app.services.apollo_connector import fetch_apollo_profiles
from app.services.scorer import score_profile
from app.services.sheets_exporter import export_to_sheets

router = APIRouter()

@router.post("/prospects")
def get_prospects(persona: PersonaInput):
    normalized = normalize(persona)

    profiles = fetch_apollo_profiles(normalized)
    matched_rows = []

    # Check for exact match in Apollo seed
    for p in profiles:
        is_match = (
            p["first_name"].lower() == normalized["first_name"].lower()
            and p["last_name"].lower() == normalized["last_name"].lower()
            and p["company"].lower() == normalized["company"].lower()
            and p["title"].lower() == normalized["title"].lower()
        )

        if is_match:
            score, _ = score_profile(p, normalized)
            matched_rows.append([
                p["first_name"],
                p["last_name"],
                p["title"],
                p["company"],
                p["location"],
                p["industry"],
                p["experience"],
                p["profile_url"],
                p.get("email") or "not available",
                p.get("phone") or "not available",
                score,
                "Apollo (Seeded)"
            ])

    #  If match found → store ONLY Apollo row(s)
    if matched_rows:
        export_to_sheets(matched_rows)
        return {"stored": "apollo", "rows": matched_rows}

    # Else → store ONLY USER row
    user_row = [[
        normalized["first_name"],
        normalized["last_name"],
        normalized["title"],
        normalized["company"],
        normalized["location"],
        normalized["industry"],
        normalized["experience"],
        normalized["profile_url"],
        normalized["email"],
        normalized["phone"],
        "-",
        "USER"
    ]]

    export_to_sheets(user_row)
    return {"stored": "user", "rows": user_row}
