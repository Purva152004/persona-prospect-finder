# def normalize(persona):
#     return {
#         "first_name": persona.first_name or "-",
#         "last_name": persona.last_name or "-",
#         "title": persona.jobTitle.lower().strip(),
#         "company": persona.company or "-",
#         "location": persona.location.lower().strip(),
#         "industry": persona.industry.lower().strip(),
#         "experience": persona.experience,
#         "profile_url": persona.profile_url or "-",
#         "email": persona.email or "-",
#         "phone": persona.phone or "-"
#     }
def normalize(persona):
    return {
        "first_name": persona.first_name.strip() if persona.first_name else "-",
        "last_name": persona.last_name.strip() if persona.last_name else "-",
        "title": persona.jobTitle.strip(),
        "company": persona.company.strip() if persona.company else "-",
        "location": persona.location.strip(),
        "industry": persona.industry.strip(),
        "experience": persona.experience,
        "profile_url": persona.profile_url or "-",
        "email": persona.email or "-",
        "phone": persona.phone or "-"
    }
