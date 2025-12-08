import streamlit as st

st.title("Tone Polisher")
draft = st.text_area("Enter a rough draft")

if st.button("Polish Tone"):
    st.write(draft.upper())