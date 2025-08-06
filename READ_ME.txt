🧠 LangGraph-Powered Python Q&A Chatbot

This project is a simple yet powerful question-answering chatbot built using LangGraph. It uses a 3-node state machine to handle user queries related to Python programming and responds with LLM-powered answers.


🔧 Tech Stack

- LangGraph – State machine-based agent framework
- ChatGroq – Fast LLM backend for responses
- Python – Core logic
- Google Colab – Execution environment
- IPython Display – For clean output formatting in Colab

📘 How It Works

The chatbot is structured using LangGraph’s `StateGraph`, with the following flow:

[Start Node] → [LLM Node] → [End Node]

- Start Node: Captures user input
- LLM Node: Uses ChatGroq to generate Python-related answers
- End Node: Displays final output in Colab via IPython


🎯 Key Features

- Structured, declarative control flow
- Easy to scale by adding tools, retries, or branching
- Clean response display inside Colab
- Uses `@tool` and typed state transitions
- Fast and responsive using Groq LLM backend


🚀 Try It Yourself

✅ Open in Google Colab: https://colab.research.google.com/drive/1E4IwYmlDhoG6Ilz2bxvHCqGD6KIVrXU8  
⚠️ Requires a valid Groq API Key (you can get one at https://console.groq.com)


📎 Example Use Cases

- “What does the error `IndexError: list index out of range` mean?”
- “Write a Python function to reverse a string.”
- “Fix this buggy code: `def add(a, b): return a - b`”


📚 What I Learned

- How to build LangGraph state workflows
- Defining memory and response logic using TypedDict
- Using tools and structured prompt flows
- Deploying and displaying results in Colab


🧩 Next Steps

- Add conditional branching for tool use
- Integrate with vector database for RAG
- Deploy via Streamlit or LangServe


👤 Author

Ali Akbar  
📍 Lahore, Pakistan  
🎓 CS Undergrad at University of Education  


⭐ If you found this useful, give it a star and connect with me — I'm actively learning and building in the Agentic AI space!
