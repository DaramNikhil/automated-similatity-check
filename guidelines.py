def enforce_guidelines(title, max_words=10):
    if len(title.split()) > max_words:
        return False, "Title exceeds maximum word limit."
    if not title[0].isupper():
        return False, "Title must start with a capital letter."
    return True, None
