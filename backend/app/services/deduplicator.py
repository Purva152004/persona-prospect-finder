def deduplicate(profiles):
    """
    Remove duplicate profiles using email or profile_url as unique key.
    """
    seen = set()
    unique = []

    for p in profiles:
        key = p.get("email") or p.get("profile_url")
        if key and key not in seen:
            seen.add(key)
            unique.append(p)

    return unique
