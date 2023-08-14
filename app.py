from summarizer import text_summarize
import streamlit as st
import PyPDF2

def read_pdf_text(pdf_file):
    text = ""
    for pdf in pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
        
    return text

def main():
    st.set_page_config(page_title="Text Summarizer", page_icon=":📄:")
    st.header("Text Summarizer")
    raw_text = ""
    st.session_state.summarize = ""
    with st.sidebar:
        option = st.selectbox('How would you like chat with PDF?', ('Upload PDF', 'Upload text'))
        if option == "Upload PDF":
            pdf_doc_url = st.file_uploader("Upload your pdf here and click on process", accept_multiple_files=True)
            with st.spinner("Proccessing"):
                if st.button("Extract Text"):
                    raw_text = read_pdf_text(pdf_doc_url)
        else:
            raw_text = st.text_area("Enter your text")
    if st.spinner("summarizer"):
        if st.button("Go") and raw_text != "":
            temp = text_summarize(raw_text, num_sentences=2)
            st.session_state.summarize = temp
    st.write(st.session_state.summarize)
    if st.session_state.summarize and st.button("reset"):
        st.session_state.summarize = ""

if __name__ == "__main__":
    main()