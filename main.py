import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

st.title("Tone Polisher")
draft = st.text_area("Enter a rough draft")

if st.button("Polish Tone"):
    # 1. Execute the API Inference Call
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a business professor who critiques their students' tone in their students' writing. For anything that your students write, you will rewrite the text to be professional and grammatically correct. The tone should be professional and academic."},
            {"role": "user", "content": draft}
        ],
        temperature=0
    )

    # 2. Parse the Response Object
    # The API returns a complex object. We must traverse it to find the text.
    polished_text = response.choices[0].message.content
    
    # 3. Render the Output
    st.write(polished_text)