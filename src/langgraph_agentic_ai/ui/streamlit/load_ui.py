import streamlit as st
from src.langgraph_agentic_ai.ui.uiconfigfile import ConfigUI


class LoadStreamlitUI:

    def __init__(self):
        self.config = ConfigUI()
        self.user_control = {}

    def load_streamlit_ui(self):

        st.set_page_config(
            page_title=self.config.get_page_title(),
            layout="wide"
        )

        st.header(self.config.get_page_title())

        with st.sidebar:

            llm_option = self.config.get_LLMs_Option()
            usecase_option = self.config.get_usecase_option()

            select_models = st.selectbox("Select LLM", llm_option)

            
            if select_models == "Groq":
                model_options = self.config.get_groq_model_option()
            elif select_models == "OpenAI":
                model_options = self.config.get_openai_model_option()
            else:
                model_options = []
                
            selected_model = st.selectbox("Select Model", model_options)
            user_control = st.selectbox("Select Usecase", usecase_option)

        return {
            "llm": select_models,
            "model": selected_model,
            "usecase": user_control
        }
