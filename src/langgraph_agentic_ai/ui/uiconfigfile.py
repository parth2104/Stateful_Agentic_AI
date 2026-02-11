from configparser import ConfigParser


class ConfigUI:

    def __init__(self, File_path=r"src\langgraph_agentic_ai\ui\uiconfig.ini"):
        self.config = ConfigParser()
        self.config.read(File_path)

    def get_LLMs_Option(self):
        return self.config["DEFAULT"].get("LLM_OPTION", "").split(",")

    def get_groq_model_option(self):
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTION", "").split(",")

    def get_openai_model_option(self):
        return self.config["DEFAULT"].get("OPENAI_MODEL_OPTION", "")

    def get_page_title(self):
        return self.config["DEFAULT"].get("PROJECT_TITLE", "AI Assistant")

    def get_usecase_option(self):
        return self.config["DEFAULT"].get("USECASE_OPTION", "").split(",")
