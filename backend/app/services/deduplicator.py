def deduplicate(profiles):
    seen = set()
    unique = []

    for p in profiles:
        key = (
            p["first_name"].lower(),
            p["last_name"].lower(),
            p["company"].lower(),
            p["location"].lower()
        )
        if key not in seen:
            seen.add(key)
            unique.append(p)

    return unique
