# from fastapi import APIRouter
# from app.schemas import PersonaInput
# from app.services.persona_normalizer import normalize
# from app.services.apollo_connector import fetch_apollo_profiles
# from app.services.scorer import score_profile
# from app.services.deduplicator import deduplicate
# from app.services.sheets_exporter import export_to_sheets

# router = APIRouter()

# @router.post("/prospects")
# def get_prospects(persona: PersonaInput):
#     normalized = normalize(persona)

#     # 1. Store persona input (formatted like Apollo)
#     export_to_sheets([[
#         normalized["first_name"],
#         normalized["last_name"],
#         normalized["title"],
#         normalized["company"],
#         normalized["location"],
#         normalized["industry"],
#         normalized["experience"],
#         normalized["profile_url"],
#         normalized["email"],
#         normalized["phone"],
#         "-",                 # score
#         "USER"               # source
#     ]])

#     # 2. Fetch Apollo profiles
#     profiles = fetch_apollo_profiles(normalized)

#     output = []
#     for p in profiles:
#         score, reason = score_profile(p, normalized)
#         output.append({
#             **p,
#             "email": p.get("email") or "not available",
#             "phone": p.get("phone") or "not available",
#             "score": score,
#             "source": "Apollo (Seeded)"
#         })

#     output = deduplicate(output)

#     if output:
#         export_to_sheets([
#             [
#                 o["first_name"], o["last_name"], o["title"], o["company"],
#                 o["location"], o["industry"], o["experience"],
#                 o["profile_url"], o["email"], o["phone"],
#                 o["score"], o["source"]
#             ] for o in output
#         ])

#     return output
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

    # ✅ 1. STORE USER ROW FIRST (IMPORTANT)
    export_to_sheets([[
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
        "-",          # score
        "USER"        # source
    ]])

    # ✅ 2. FETCH SEEDED APOLLO DATA
    profiles = fetch_apollo_profiles(normalized)

    output = []

    for p in profiles:
        score, reason = score_profile(p, normalized)
        output.append({
            **p,
            "email": p.get("email") or "not available",
            "phone": p.get("phone") or "not available",
            "score": score,
            "source": "Apollo (Seeded)"
        })

    output = deduplicate(output)
    output.sort(key=lambda x: x["score"], reverse=True)

    # ✅ 3. STORE APOLLO ROWS
    if output:
        rows = [[
            o["first_name"],
            o["last_name"],
            o["title"],
            o["company"],
            o["location"],
            o["industry"],
            o["experience"],
            o["profile_url"],
            o["email"],
            o["phone"],
            o["score"],
            o["source"]
        ] for o in output]

        export_to_sheets(rows)

    return output
