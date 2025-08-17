"""Define a custom Reasoning and Action agent.

Works with a chat model with tool calling support.
"""

from utils import load_chat_model
from prompts import SYSTEM_PROMPT
from state import InputState
from langgraph.prebuilt import create_react_agent
from langgraph.graph import StateGraph, START, END


agent = create_react_agent(
    model=load_chat_model(),  
    tools=[],  
    prompt=SYSTEM_PROMPT
)

graph_builder = StateGraph(InputState)

graph_builder.add_node("agent", agent)

graph_builder.add_edge(START, "agent")
graph_builder.add_edge("agent", END)

graph = graph_builder.compile()



