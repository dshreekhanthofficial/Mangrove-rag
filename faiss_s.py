import os
import pickle
import re
import numpy as np
from langchain_community.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
INDEX_PATH = "mangrove_index.faiss"
PICKLE_PATH = "mangrove_store.pkl"

def pre_doc(path):
    # Use PyPDFLoader to load the PDF document
    loader = PyPDFLoader(path)
    file = loader.load()

    # Use RecursiveCharacterTextSplitter to split the document into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    texts = text_splitter.split_documents(file)
    texts_content = [doc.page_content for doc in texts]
    
    return texts_content

def load_Faiss(texts, update_existing=False):

    # 🔹 Flatten nested lists (from multiple PDFs)
    if isinstance(texts, list) and any(isinstance(t, list) for t in texts):
        texts = [item for sublist in texts for item in sublist]

    if os.path.exists(INDEX_PATH) and os.path.exists(PICKLE_PATH):
        faiss_index = FAISS.load_local(INDEX_PATH, embedding_model, allow_dangerous_deserialization=True)

        if update_existing:
            # print("📄 Adding new document to existing FAISS store...")
            new_store = FAISS.from_texts(texts, embedding_model)
            faiss_index.merge_from(new_store)
            faiss_index.save_local(INDEX_PATH)
            with open(PICKLE_PATH, "ab") as f:
                pickle.dump(texts, f)
            # print("✅ FAISS store updated with new document.")
        return faiss_index

    # If FAISS doesn’t exist yet, create a new one
    # print("🆕 Creating new FAISS index...")
    faiss_index = FAISS.from_texts(texts, embedding_model)
    faiss_index.save_local(INDEX_PATH)
    with open(PICKLE_PATH, "wb") as f:
        pickle.dump(texts, f)
    # print("✅ New FAISS store created.")
    return faiss_index

def keyword_relevance(text: str, threshold: int = 5) -> bool:

    keywords = [
        "mangrove", "estuaries", "salt-tolerant", "brackish", "tidal",
        "wetlands", "mudflats", "coastal forest", "delta", "Rhizophora",
        "Avicennia", "Sonneratia", "Aegiceras", "ecosystem", "coastal vegetation",
        "prop roots", "pneumatophores", "marine biodiversity", "sediment retention",
        "coastal erosion", "carbon sequestration", "nursery habitat",
        "intertidal", "mangrove swamp", "brackish water", "aquatic species",
        "coastal protection", "blue carbon", "saline soil"
    ]
    text_lower = text.lower()
    count = sum(len(re.findall(rf"\b{k}\b", text_lower)) for k in keywords)
    return count >= threshold

def is_relevant_to_mangroves(text: str, threshold: float = 0.45) -> bool:

    topic = (
        "Mangrove forests are unique coastal ecosystems found in tropical and subtropical regions. "
        "They are salt-tolerant trees that thrive in intertidal zones, playing crucial roles in shoreline protection, "
        "carbon sequestration, sediment trapping, and biodiversity conservation. "
        "Mangroves serve as breeding and nursery grounds for many aquatic species and act as a natural barrier against "
        "coastal erosion and storm surges. This topic includes the ecology, biodiversity, restoration, conservation, "
        "and socio-economic importance of mangrove forests."
    )

    # Compute embeddings and cosine similarity
    topic_emb = embedding_model.embed_query(topic)
    doc_emb = embedding_model.embed_query(text[:3000])  # sample first 3k chars for efficiency
    sim = np.dot(topic_emb, doc_emb) / (np.linalg.norm(topic_emb) * np.linalg.norm(doc_emb))

    return sim >= threshold

def is_relevant(text: str) -> bool:
   
    return is_relevant_to_mangroves(text)
