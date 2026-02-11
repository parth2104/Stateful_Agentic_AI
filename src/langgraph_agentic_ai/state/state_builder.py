from pydantic import BaseModel
from langchain_core.messages import BaseMessage 
from langgraph.graph.message import add_messages 
from typing import Annotated
from typing_extensions import List 





class State(BaseModel):
    """
    Represent the structure of the state in graph
    """
    messages: Annotated [List[BaseMessage],add_messages]

