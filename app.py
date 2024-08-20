# pdf_password_app.py

import streamlit as st
from PyPDF2 import PdfReader, PdfWriter
import io

# Function to set password on a PDF
def set_password(pdf_file, password):
    pdf_reader = PdfReader(pdf_file)
    pdf_writer = PdfWriter()

    for page_num in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page_num])

    pdf_writer.encrypt(user_password=password)

    output = io.BytesIO()
    pdf_writer.write(output)
    output.seek(0)
    return output

# Streamlit app
st.title("PDF Password Protection")

st.write("Upload a PDF file and set a password to protect it.")

# Upload PDF file
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Input password
    password = st.text_input("Enter password", type="password")

    if st.button("Set Password"):
        if password:
            # Process PDF
            protected_pdf = set_password(uploaded_file, password)
            
            # Provide download link
            st.download_button(
                label="Download Protected PDF",
                data=protected_pdf,
                file_name="protected_output.pdf",
                mime="application/pdf"
            )
            st.success("Password set successfully!")
        else:
            st.error("Please enter a password.")
