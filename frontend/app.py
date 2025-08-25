import os
import requests
import streamlit as st

API_URL = os.getenv("API_URL", "http://localhost:8000")

st.title("Loan Assistant Chat")

user_question = st.text_input("Ask a question about loans:")

if st.button("Send"):
    with st.spinner("Thinking..."):
        res = requests.post(
            f"{API_URL}/chat",
            json={"query": user_question}
        )
        if res.status_code == 200:
            st.success(res.json()["answer"])
        else:
            st.error(f"Error {res.status_code}: {res.text}")