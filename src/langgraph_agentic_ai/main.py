import streamlit as st
from src.langgraph_agentic_ai.ui.streamlit.load_ui import LoadStreamlitUI
from src.langgraph_agentic_ai.LLMs.llm import LLM
from src.langgraph_agentic_ai.graphs.graph_builder import GraphBuilder


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

    if user_message:
        try:
            llm_config=LLM(user_control_input=user_input)
            model=llm_config.get_llm_model()

            if not model:
                st.error("LLM model could not be initialise")
                return
            use_case=user_input.get("usecase")

            if not use_case:
                st.error("use case is not selected")
                return
            
            graph_builder=GraphBuilder(model)

            graph=graph_builder.setup_graph(use_case)
            

        except Exception as e:
            pass
