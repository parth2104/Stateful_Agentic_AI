import streamlit as st
from src.langgraph_agentic_ai.ui.streamlit.load_ui import LoadStreamlitUI


def load_langgraph_agentic_ai():
    """
    Load and run the agentic ai application 
    """

    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Failed to load user input")
        return

    user_message = st.chat_input("Enter your message")
