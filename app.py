import streamlit as st
from extract import extract_text_from_pdf
from notion_integration import save_to_notion
import tempfile
import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

st.title("📄 PDF Workflow")
st.write("Extract, process, and organize PDFs with Claude + Notion")

client = Anthropic()

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    st.success("PDF uploaded!")
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.getbuffer())
        tmp_path = tmp.name
    
    text = extract_text_from_pdf(tmp_path)
    
    st.write("**Extracted Text:**")
    st.text(text[:500])
    
    st.subheader("🤖 Process with Claude")
    
    task = st.selectbox("Choose task:", ["summarize", "extract_entities", "organize"])
    
    if st.button("Process with Claude"):
        with st.spinner("Processing..."):
            prompts = {
                "summarize": "Summarize this text in 3 bullet points:",
                "extract_entities": "Extract key entities (people, dates, numbers) from this text:",
                "organize": "Organize this content into a structured format:"
            }
            
            prompt = prompts.get(task, "Summarize this text:")
            
            message = client.messages.create(
                model="claude-haiku-4-5-20251001",
                max_tokens=1024,
                messages=[
                    {"role": "user", "content": f"{prompt}\n\n{text}"}
                ]
            )
            
            result = message.content[0].text
            st.success("✅ Claude Response:")
            st.write(result)
            
            # Save to Notion
            with st.spinner("Saving to Notion..."):
                success = save_to_notion(
                    title=uploaded_file.name,
                    content=text[:500],
                    task=task,
                    claude_response=result
                )
                
                if success:
                    st.success("✅ Saved to Notion!")
                else:
                    st.error("❌ Failed to save to Notion")
    
    os.remove(tmp_path)