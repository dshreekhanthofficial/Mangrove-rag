💬 Chat With Me 🤖

Welcome to Chat With Me, an intelligent conversational AI system that combines the power of LangChain and Google’s Gemini LLM to deliver context-aware and knowledge-driven chatbot experiences.

This project leverages both Predefined RAG (Retrieval-Augmented Generation) and Knowledge-Based RAG to enable seamless interactions based on static and dynamic data sources.

🌟 Project Overview

Chat With Me allows users to engage in meaningful conversations powered by cutting-edge AI.
It can retrieve relevant information from uploaded documents, predefined knowledge bases, and respond naturally using Gemini’s advanced reasoning and generation capabilities.

🧠 Dual RAG Architecture

Predefined RAG — Utilizes preloaded datasets or fixed domain knowledge for consistent, factual responses.

Knowledge-Based RAG — Allows users to upload PDFs or custom data, enabling dynamic, document-based question answering.

🚀 Key Features

✅ Conversational Intelligence: Natural, human-like responses using Google’s Gemini LLM.
✅ PDF Interaction: Upload documents and ask questions directly about their content.
✅ Hybrid RAG Model: Combines predefined and user-provided knowledge bases for enhanced retrieval.
✅ LangChain Integration: Manages data processing, vector storage, and context retrieval efficiently.
✅ User-Friendly Interface: Simple chat interface for easy and intuitive interaction.


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
