# Import necessary libraries
import streamlit as st
from llm2 import llm

# Set the title of the Streamlit app
st.title("Chat with me 🤖")

# Initialize chat history
if "messagesgem" not in st.session_state:
    st.session_state.messagesgem = []

# Display chat messages from history on app rerun
for message in st.session_state.messagesgem:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if query := st.chat_input("What is up?", key="Gem"):
    # Display user message in chat message container
    st.chat_message("user").markdown(query)
    # Add user message to chat history
    st.session_state.messagesgem.append({"role": "user", "content": query})
    # Retrieve the response from palm
    response = llm(query)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messagesgem.append({"role": "assistant", "content": response})
    