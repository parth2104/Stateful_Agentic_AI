# Stateful Agentic AI

Stateful Agentic AI is a graph-based intelligent agent system built using LangChain and LangGraph that enables multi-step reasoning, persistent memory, and dynamic workflow orchestration. The system maintains contextual state across interactions and supports modular, extensible AI-driven decision making.

---

## Overview

This project demonstrates how to design and implement a stateful AI agent architecture capable of:

- Managing persistent conversational state
- Executing multi-node reasoning workflows
- Orchestrating tool invocation dynamically
- Supporting scalable backend integration
- Providing an interactive frontend interface

The system uses a graph-driven execution model where nodes represent reasoning steps or tools, and edges define state transitions between them.

---

## Architecture

### Core Technologies

- Python
- LangChain (LLM orchestration and tool integration)
- LangGraph (graph-based workflow and state management)
- Streamlit (frontend UI)
- Flask (backend API layer)

### System Design

1. User interacts with the Streamlit interface.
2. The request is forwarded to the Flask backend.
3. LangGraph orchestrates the execution flow using a defined graph structure.
4. LangChain manages LLM invocation and tool usage.
5. The system updates and persists the state.
6. A context-aware response is returned to the user.

The architecture is modular and supports extensibility for additional nodes, tools, and workflows.

---

## Key Features

- Stateful conversation management
- Graph-based workflow orchestration
- Multi-step reasoning execution
- Tool invocation support
- Modular LLM integration
- Backend API handling with Flask
- Interactive user interface with Streamlit
- Extensible agent design

---

## Project Structure

│
├── app.py # Streamlit frontend application
├── api.py # Flask backend service
│
├── state/ # State management layer
│ ├── state_builder.py # Defines State schema and state handling
│ └── state_types.py # Message and state type definitions
│
├── nodes/ # Agent node definitions
│ ├── basic_chatbot_node.py # Core chatbot node logic
│ └── tool_node.py # Tool execution node (if applicable)
│
├── implementations/ # Node implementations
│ └── basic_chatbot_node.py # Concrete implementation of chatbot node
│
├── workflows/ # Graph workflow definitions
│ └── graph_builder.py # Builds and compiles LangGraph workflows
│
├── llm/ # LLM configuration and builder
│ └── llm_builder.py # Model selection and LLM initialization
│
├── requirements.txt # Project dependencies
└── README.md # Project documentation