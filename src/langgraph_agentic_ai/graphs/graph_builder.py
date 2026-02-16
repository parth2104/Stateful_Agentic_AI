from langgraph.graph  import StateGraph,START,END
from src.langgraph_agentic_ai.state.state_builder import State 
from src.langgraph_agentic_ai.nodes.chatbot_node import BasicChatbotNode





class GraphBuilder:

    def __init__(self,model):
        self.model=model
        self.graph=StateGraph(State)

    def build_chatbot(self):

        self.basic_chabot_bode=BasicChatbotNode(self.model)

        self.graph.add_node("chatbot",self.basic_chabot_bode.process)
        self.graph.add_edge(START,"chatbot")
        self.graph.add_edge("chatbot",END)

    def setup_graph(self,usecase):
        if usecase == "Basic Chatbot":
            self.build_chatbot()
