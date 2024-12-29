import streamlit as st
import json
from similarity import check_similarity
from guidelines import enforce_guidelines

DATA_FILE = "titles.json"

def load_titles():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_title(new_title):
    titles = load_titles()
    titles.append(new_title)
    with open(DATA_FILE, "w") as file:
        json.dump(titles, file)

st.title("Automated Similarity Check and Guideline Enforcement")

new_title = st.text_input("Enter a new title:", "")

if new_title:
    existing_titles = load_titles()

    is_unique, similarity = check_similarity(new_title, existing_titles)

    if not is_unique:
        st.error(f"Title is too similar to an existing title (Similarity: {similarity}%).")
    else:
        st.success(f"Title is unique (Similarity: {similarity}%)")
        
    guidelines_ok, message = enforce_guidelines(new_title)
    if not guidelines_ok:
        st.warning(f"Guideline Error: {message}")
    else:
        st.success("Title complies with all guidelines.")

if st.button("Submit"):
    if new_title:
        existing_titles = load_titles()

        is_unique, similarity = check_similarity(new_title, existing_titles)
        if not is_unique:
            st.error(f"Title is too similar to an existing title (Similarity: {similarity}%).")
        else:
            guidelines_ok, message = enforce_guidelines(new_title)
            if not guidelines_ok:
                st.warning(f"Guideline Error: {message}")
            else:
                # Save the title
                save_title(new_title)
                st.success("Title accepted and added successfully!")
                st.write("**Existing Titles:**")
                st.write(existing_titles)
