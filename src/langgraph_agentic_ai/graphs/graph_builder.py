from langgraph.graph  import StateGraph,START,END
from src.langgraph_agentic_ai.state.state_builder import State 









class GraphBuilder:

    def __init__(self,model):
        self.model=model
        self.graph=StateGraph(State)

    def build_chatbot(self):

        self.graph.add_node("chatbot","")
        self.graph.add_edge(START,"chatbot")
        self.graph.add_edge("chatbot",END)
