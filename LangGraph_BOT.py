# Install necessary libraries
%pip install -U --quiet langgraph langchain-groq

# Import necessary libraries
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_groq import ChatGroq
from google.colab import userdata
import os

# Define the state for the graph
class State(TypedDict):
  messages:Annotated[list, add_messages]

# Initialize the StateGraph
Graph_Builder = StateGraph(State)

# Retrieve API keys and set environment variables
# Ensure you have added 'groq_API', 'langSmith_key' to Colab's secrets manager
groq_api = userdata.get('groq_API')
langsmith_key = userdata.get("langSmith_key")

os.environ["langChain_API_key"] = langsmith_key
os.environ["langChain_TRACING_V2"] = "true"
os.environ["Project_Name"] = "Practicing_LangChain"

# Initialize the language model
llm = ChatGroq(groq_api_key=groq_api, model_name= "Gemma2-9b-It")

# Define the chatbot function
def chatbot(state:State):
  return {"messages":llm.invoke(state['messages'])}

# Add node and edges to the graph
Graph_Builder.add_node("chatbot",chatbot)
Graph_Builder.add_edge(START,"chatbot")
Graph_Builder.add_edge("chatbot",END)

# Compile the graph
graph = Graph_Builder.compile()

# Run the chatbot
while True:
  user_input = input("User:")
  if user_input.lower() in ["quit", "q"]:
    print("Good Bye")
    break
  for event in graph.stream({'messages':("user",user_input)}):
    event_values = event.values()
    for value in event_values:
      print("Assistant: ", value["messages"].content)