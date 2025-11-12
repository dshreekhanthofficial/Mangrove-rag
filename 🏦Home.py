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
st.header("Welcome! to Project X 🌐🤖")
st.markdown(
    """
    Unlock the Power of Language Models and AI
    ### What This Application Offers
    ## 1. LangChain-Powered Question Answering 🦜️🔗
    Harness the capabilities of LangChain to extract meaningful insights from your PDF documents. Simply upload your PDF, and the intelligent system powered by 
    Google's state-of-the-art language model will provide accurate and relevant answers to your questions.
    ## 2. Interactive Google LLM UI 🌴
    Engage with the latest in AI technology through a user-friendly interface. Interact seamlessly with Google's Gemini Language Model to explore its vast knowledge base,
    generate creative content, and experience the future of language understanding.
    ### Key Features 🌟
    - **Effortless PDF Interaction**: Ask questions about your uploaded PDFs, and this system will provide concise and precise answers.
    - **Cutting-Edge Language Model**: Utilize Google's Gemini for natural language processing, content generation, and a wide range of AI-driven tasks.
    - **User-Friendly Interface**: Navigate through the application with ease, making AI interaction accessible to all users.
    ## How It Works ⚙️

    1. **Upload Your PDF**: Use the intuitive interface to upload your PDF document.

    2. **Ask Questions**: Pose questions related to your document and receive instant, accurate answers.

    3. **Explore Gemini LLM**: Dive into the world of AI with our interactive interface powered by Google's Gemini Language Model.
    
    ### Get Started Today! 🚀
    Unleash the potential of machine learning and artificial intelligence.\n 
    ***👈 Select a service from the sidebar***
"""
)
