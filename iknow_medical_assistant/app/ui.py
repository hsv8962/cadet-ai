# ui.py - placeholder for initial implementation
import streamlit as st
from .chatbot import get_chatbot_response
from .parser import extract_text_from_pdf
from .config import APP_NAME, VERSION

def main():
    st.set_page_config(page_title=APP_NAME, page_icon="🩺")

    # Title and Subtitle
    st.markdown(f"""
    <h1 style='text-align: center;'>🩺 {APP_NAME}</h1>
    <p style='text-align: center;'>Ask any medical question. Responses are generated locally using LLaMA 3 via Ollama.</p>
    <p style='text-align: center; font-size: small;'>Version: <code>{VERSION}</code></p>
    """, unsafe_allow_html=True)

    # User input
    user_input = st.text_input("🤖 You:", placeholder="What causes high cholesterol")

    # Display answer
    if st.button("Send") and user_input:
        with st.spinner("Thinking..."):
            response = get_chatbot_response(user_input)
            st.markdown("""<hr style='margin-top: 2em;'>""", unsafe_allow_html=True)
            st.markdown(f"**iKnow:** {response}")

    # Optional PDF upload placeholder
    st.sidebar.header("Upload EMR")
    uploaded_file = st.sidebar.file_uploader("Upload a PDF or EMR file", type=["pdf"])
    if uploaded_file:
        extracted_text = extract_text_from_pdf(uploaded_file)
        st.sidebar.success("PDF parsed successfully!")
        st.sidebar.write(extracted_text[:1000])  # Preview first 1000 characters
