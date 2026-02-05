
def normalize(persona):
    return {
        "title": persona.jobTitle.lower(),
        "experience": persona.experience,
        "location": persona.location.lower(),
        "industry": persona.industry.lower(),
        "keywords": persona.keywords or []
    }
