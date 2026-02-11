from src.langgraph_agentic_ai.state.state_builder import State 





class BasicChatbotNode:

    def __init__(self,model):

        self.model=model
    
    def process(self,state:State):
        """
        it is the functionality of node how it is works and give the result
        """

        return {"messages":self.model.invoke(state.messages)}
