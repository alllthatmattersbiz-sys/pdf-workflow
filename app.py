import streamlit as st
from extract import extract_text_from_pdf
import tempfile
import os

st.title('📄 PDF Workflow')
st.write('Extract, process, and organize PDFs')

uploaded_file = st.file_uploader('Upload a PDF', type='pdf')

if uploaded_file:
    st.success('PDF uploaded!')
    
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp:
        tmp.write(uploaded_file.getbuffer())
        tmp_path = tmp.name
    
    text = extract_text_from_pdf(tmp_path)
    
    st.write('**Extracted Text:**')
    st.text(text[:500])
    
    os.remove(tmp_path)
