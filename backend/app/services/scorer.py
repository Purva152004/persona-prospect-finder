def score_profile(profile, persona):
    score = 0
    reasons = []

    if persona["title"] in profile["title"].lower():
        score += 30
        reasons.append("Title match")

    if persona["location"] in profile["location"].lower():
        score += 20
        reasons.append("Location match")

    if persona["industry"] in profile["industry"].lower():
        score += 20
        reasons.append("Industry match")

    if profile["experience"] >= persona["experience"]:
        score += 30
        reasons.append("Experience match")

    return score, ", ".join(reasons)
