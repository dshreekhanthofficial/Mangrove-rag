# Import necessary library
import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="🏦Home",
)

# Display sidebar message and snow animation
st.sidebar.success("Select a Service above.")
st.sidebar.snow()

# Display header and project introduction
st.header("Welcome! to*MangroveSense,")
st.markdown(
    """
   # 🌿 *MangroveSense: Intelligent Chatbot for Mangrove Ecosystems*

Welcome to **MangroveSense**, an AI-powered conversational system crafted to explore and explain the fascinating world of **Mangrove Forests** 🌊🌴.  
Powered by **Google’s Gemini LLM** and **LangChain**, MangroveSense combines knowledge retrieval and natural dialogue to deliver accurate, insightful, and eco-focused conversations.

---

## 🧭 *Project Overview*

**MangroveSense** is designed to answer questions *exclusively related to Mangrove Forests* — including their **flora, fauna, conservation, economic impact, and tourism**.  
It intelligently fuses **Gemini’s reasoning** abilities with a **dual-RAG (Retrieval-Augmented Generation)** architecture, ensuring each response is both contextually relevant and scientifically grounded.

---

## 🧠 *Dual RAG Architecture*

### 🌱 1. Predefined RAG  
- Uses a **preloaded knowledge base** derived from curated PDFs and verified research on mangroves.  
- Data is **pre-processed and embedded** into a **Faiss vector store** for efficient semantic retrieval.  
- Ensures reliable, factual responses grounded in authoritative environmental knowledge.

### 📚 2. Knowledge-Based RAG  
- Lets users **upload their own documents** to dynamically expand the chatbot’s knowledge base.  
- Each uploaded file is **checked for topic relevance** — only mangrove-related content is added.  
- Unrelated documents trigger a **polite warning message**, preserving the project’s ecological focus and domain integrity.

---

## 💬 *General Gemini Mode*

This secondary mode uses **Gemini LLM** *without RAG*, relying purely on its internal context and reasoning.  
It provides **high-quality conversational insights** while remaining strictly focused on **Mangrove Forests** and their ecosystem.

---

## 🚀 *Key Features*

✅ **Mangrove-Only Expertise** — Responds exclusively to environmental and mangrove-related topics.  
✅ **Hybrid Knowledge Integration** — Combines static (predefined) and dynamic (user-uploaded) data sources.  
✅ **Automated Filtering** — Adds only relevant mangrove content to the vector database.  
✅ **LangChain + Faiss** — Enables fast, context-aware document retrieval.  
✅ **Gemini-Powered Reasoning** — Produces natural, coherent, and factual responses.  
✅ **Streamlit UI** — Clean, simple, and eco-themed user interface for smooth user experience.

---

## 🌊 *How It Works*

1. **Upload Your PDF** — Add mangrove-related research papers or reports.  
2. **Ask Questions** — Get precise answers based on retrieved document chunks.  
3. **Switch Modes** — Use Predefined RAG, Knowledge-Based RAG, or Gemini-only chat for flexible interaction.

---

### 🌴 *Why MangroveSense?*

Mangrove forests are vital to coastal ecosystems — protecting shorelines, storing carbon, and supporting biodiversity.  
*MangroveSense* empowers researchers, students, and enthusiasts to explore these ecosystems through the lens of artificial intelligence.

---

### 🌟 *Get Started Today!*

Unleash the power of **AI and environmental intelligence**.  
***👈 Select a feature from the sidebar to begin your journey with MangroveSense!***
"""
)
