import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

st.title("Tone Polisher")
draft = st.text_area("Enter a rough draft")

if st.button("Polish Tone"):
    st.write(draft.title())