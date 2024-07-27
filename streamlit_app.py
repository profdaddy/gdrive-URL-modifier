import streamlit as st
import re


download_URL = ""

def make_downloadable_GDrive_URL():
    
    if st.session_state.copy_mode == "Make Copyable":
        make_copyable_GDrive_URL()
    else:
        download_string = "https://drive.google.com/uc?export=download&id="

        file_id_regex = r"\/d\/(.*)\/"

        file_id_match = re.findall(file_id_regex, st.session_state['URL'])

        if file_id_match != []:        
            st.session_state["download_URL"] = download_string + file_id_match[0]

def make_copyable_GDrive_URL():
    new_URL = original_URL_text.replace("edit", "copy")
    st.session_state["download_URL"] = new_URL

if "download_URL" not in st.session_state:
   st.session_state.download_URL = "Modified URL will appear here"

with st.form("URL Form", clear_on_submit=True):
    original_URL_text = st.text_input("Enter URL to modify", key='URL')
    
    replacement_mode = st.radio(
        "Replacement mode",
        ['Make Downloadable', "Make Copyable"], 
        index = 0, 
        horizontal=True,
        key='copy_mode'
    )

    st.divider()
    downloadable_URL_text = st.code(st.session_state.download_URL)
    submitted = st.form_submit_button("Submit", on_click=make_downloadable_GDrive_URL)

