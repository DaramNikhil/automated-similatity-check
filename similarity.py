from rapidfuzz import fuzz

def check_similarity(new_title, existing_titles, threshold=80):
    for existing_title in existing_titles:
        similarity = fuzz.ratio(new_title.lower(), existing_title.lower())
        if similarity >= threshold:
            return False, similarity
    return True, 0
