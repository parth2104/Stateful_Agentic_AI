import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv  
load_dotenv()


class LLM:

    def __init__(self,user_control_input):
        self.user_control_input=user_control_input

    def get_llm_model(self):
        try:
            if self.user_control_input["selected_LLM"] ==  "Groq":
                return ChatGroq(model=self.user_control_input["selected_groq_model"],temperature=0.5)
            elif self.user_control_input["selected_LLM"] == "OpenAI":
                return ChatOpenAI(model=self.user_control_input["selected_openai_model"],temperature=0.5)
        except Exception as e:
            raise ValueError(f"Error Occured with the value :{e}")