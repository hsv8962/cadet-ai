# parser.py - placeholder for initial implementation

import fitz  # PyMuPDF
import streamlit as st  # Required to show sidebar errors in Streamlit

def extract_text_from_pdf(pdf_file) -> str:
    """
    Extracts all text content from the given PDF file.

    Parameters:
        pdf_file (UploadedFile): The file object uploaded via Streamlit.

    Returns:
        str: Combined extracted text from all PDF pages.
    """
    try:
        doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
        extracted_text = ""
        for page in doc:
            extracted_text += page.get_text()
        doc.close()
        return extracted_text.strip()

    except Exception as e:
        st.sidebar.error(f"Failed to read PDF: {e}")
        return ""  # Return an empty string if extraction fails

