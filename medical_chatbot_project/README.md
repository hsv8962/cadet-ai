# iKnow Medical Assistant Chatbot

A locally hosted AI chatbot for basic medical inquiries using:
- LangChain
- Streamlit
- Ollama (LLaMA 3)

## 🔧 Setup Instructions

1. Make sure Ollama is installed and running:
   https://ollama.com

```bash
ollama run llama3
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Run the chatbot:

```bash
streamlit run medical_chatbot_app.py
```

This app runs 100% offline using your local LLaMA 3 model.
