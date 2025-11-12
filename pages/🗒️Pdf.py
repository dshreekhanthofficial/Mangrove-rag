# Import necessary libraries
import streamlit as st
from llm import query_llm
from faiss_s import load_Faiss, pre_doc, is_relevant
import os

# Set the title of the Streamlit app
st.title("Q Gemini 🤖")

# Sidebar for file upload
with st.sidebar:
    st.header("FILE UPLOAD")
    pdf = st.file_uploader("Supported document: PDF")
    st.info(
        "Please submit your additional PDF document here. Processing time increases with the document's size. "
        "Ask questions related to the document's content for best results.",
        icon='💡'
    )

    # Define folder paths
    folder_path = "Books"
    os.makedirs(folder_path, exist_ok=True)
    faiss_path = r"mangrove_index.faiss"

    # Cache resource for FAISS load
    @st.cache_resource(show_spinner=False)
    def process_faiss():

        pdf_texts = []
        for file in os.listdir(folder_path):
            if file.endswith(".pdf"):
                pdf_texts.append(pre_doc(os.path.join(folder_path, file)))

        doc_search = load_Faiss(pdf_texts)
        # print("--------------Docs Search:",doc_search)
        st.success("✅ Vector store loaded successfully!")
        return doc_search

    # If FAISS exists, load it
    if os.path.exists(faiss_path):
        st.write("📂 Loading existing FAISS index...")
        doc_search = process_faiss()
    else:
        st.write("🆕 Creating FAISS index from PDFs in 'Books'...")
        doc_search = process_faiss()

    # If a new PDF is uploaded
    if pdf is not None:
        file_path = os.path.join(folder_path, pdf.name)
        with open(file_path, "wb") as f:
            f.write(pdf.getbuffer())

        with st.status("Validating uploaded document...", state="running", expanded=False) as status:
            new_text = pre_doc(file_path)
            if isinstance(new_text, list):
                new_text = " ".join(new_text)
            # print("------------------New text:",new_text)
            st.write("Checking if document is relevant to Mangrove forests...")

            if is_relevant(new_text):
                st.write("✅ The document is relevant. Adding to FAISS index...")
                doc_search = load_Faiss([new_text], update_existing=True)
                status.update(label="✅ Document added to FAISS index", state="complete")
                st.success("✅ Document added and FAISS index updated!")
            else:
                status.update(label="⚠️ Irrelevant document skipped", state="error", expanded=True)
                st.warning("🚫 The uploaded document is not about Mangrove forests and was skipped.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if query := st.chat_input("Question related to your document..."):
    # Display user messageAsk a qu
    st.chat_message("user").markdown(query)
    st.session_state.messages.append({"role": "user", "content": query})

    # Get LLM response
    response = query_llm(query, doc_search)

    # Display assistant message
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
