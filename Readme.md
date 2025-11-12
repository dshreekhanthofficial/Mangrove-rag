💬 Chat With Me 🤖

# 🌿 *MangroveSense: Intelligent Chatbot for Mangrove Ecosystems*

Welcome to *MangroveSense, an AI-powered conversational system crafted to explore and explain the fascinating world of **Mangrove Forests* 🌊🌴.  
Powered by *Google’s Gemini LLM* and *LangChain*, MangroveSense combines knowledge retrieval and natural dialogue to deliver accurate, insightful, and eco-focused conversations.

---

## 🧭 *Project Overview*

*MangroveSense* is designed to answer questions exclusively related to Mangrove Forests — including their flora, fauna, conservation, economic impact, and tourism.  
It intelligently fuses *Gemini’s reasoning* abilities with a *dual-RAG (Retrieval-Augmented Generation)* architecture, ensuring each response is both contextually relevant and scientifically sound.

---

## 🧠 *Dual RAG Architecture*

### 🌱 1. Predefined RAG  
- Uses a *preloaded knowledge base* derived from curated PDFs and research on mangroves.  
- The data is *pre-extracted and embedded* into a *Faiss vector store* for efficient retrieval.  
- Ensures reliable, factual responses grounded in verified environmental knowledge.

### 📚 2. Knowledge-Based RAG  
- Lets users *upload their own documents* to expand the chatbot’s knowledge dynamically.  
- Before embedding, the uploaded file is *checked for relevance* — only mangrove-related content is added.  
- If a file is unrelated, the system displays a polite *warning message*, ensuring domain integrity.

---

## 💬 *General Gemini Mode*

This secondary mode uses *Gemini LLM without RAG*, responding purely from its predefined prompt context.  
It offers *high-quality, conversational insights* while adhering strictly to the topic of *Mangrove Forests*.

---

## 🚀 *Key Features*

✅ *Mangrove-Only Expertise* — Responds only to relevant environmental topics.  
✅ *Hybrid Knowledge Integration* — Combines static (predefined) and dynamic (uploaded) sources.  
✅ *Automated Filtering* — Ensures only mangrove-related content enriches the database.  
✅ *LangChain + Faiss* — Efficient vector storage and semantic retrieval.  
✅ *Gemini-Powered Reasoning* — Human-like, context-aware explanations.  
✅ *User-Friendly Interface* — Clean and simple chat experience via Streamlit.

---

🌿 MangroveSense — where AI meets environmental intelligence.


### Installation Guide 🛠️💻
To install the required dependencies, execute the following command in your terminal:

```bash
pip install -r requirements.txt
```


### Configuration Setup 🔐📝
Create a `.env` file in the project root or/and add the following content, replacing placeholders with your actual API keys:

```env
GOOGLE_API_KEY='Enter Your Gemini Api Here' # You can create one from makersuite.google.com
```
```


### Launch the AI Symphony 🎶🚀
To start the main Streamlit app, run the following command:

```bash
streamlit run 🏦Home.py
```


### Important Note 📌📘
Make sure to create a folder named **Books** and place the document (PDF you need to query) inside it.

Prepare to be amazed by the wonders of AI with Project X!
