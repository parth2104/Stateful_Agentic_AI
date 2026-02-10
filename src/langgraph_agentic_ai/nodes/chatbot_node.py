from src.langgraph_agentic_ai.state.state_builder import State 
from langchain_core.messages import BaseMessage




class BasicChatbotNode:

    def __init__(self,model):

        self.model=model
    
    def basic_chatbot(self,state:State):

        return {"messages":self.model.invoke(State["messages"])}
