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
            use_case_option = self.config.get_usecase_option()

            self.user_control["selected_LLM"] = st.selectbox(
                "Select LLM", llm_option
            )

            if self.user_control["selected_LLM"] == "Groq":
                model_options = self.config.get_groq_model_option()
                self.user_control["selected_groq_model"] = st.selectbox(
                    "Select model", model_options
                )

            elif self.user_control["selected_LLM"] == "OpenAI":
                model_options = self.config.get_openai_model_option()
                self.user_control["selected_openai_model"] = st.selectbox(
                    "Select model", model_options
                )

            self.user_control["usecase"] = st.selectbox(
                "Select the use case", use_case_option
            )

        return self.user_control
