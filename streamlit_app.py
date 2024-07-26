import streamlit as st
import re


download_URL = ""

def make_downloadable_GDrive_URL():
    download_string = "https://drive.google.com/uc?export=download&id="

    file_id_regex = r"\/d\/(.*)\/"

    file_id_match = re.findall(file_id_regex, original_URL_text)
    print("Text:", original_URL_text)

    if file_id_match != []:        
        st.session_state["download_URL"] = download_string + file_id_match[0]

if "download_URL" not in st.session_state:
   st.session_state.download_URL = "Modified URL will appear here"




with st.form("URL Form"):
    original_URL_text = st.text_input(" ", value="Enter URL to modify", label_visibility="hidden")
    downloadable_URL_text = st.code(st.session_state.download_URL)
    submitted = st.form_submit_button("Submit", on_click=make_downloadable_GDrive_URL)

