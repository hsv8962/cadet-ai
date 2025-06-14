import streamlit as st
from langchain_community.llms import Ollama
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

st.set_page_config(page_title="iKnow Medical Assistant", page_icon="🩺", layout="wide")
st.title("🩺 iKnow Medical Assistant")
st.markdown("Ask any medical question. Responses are generated locally using LLaMA 3 via Ollama.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    st.session_state.chain = ConversationChain(
        llm=Ollama(model="llama3"),
        memory=ConversationBufferMemory()
    )

user_input = st.text_input("👨‍⚕️ You:", placeholder="What causes high blood pressure?", key="user_input")
if st.button("Send") and user_input:
    response = st.session_state.chain.run(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("iKnow", response))

if st.session_state.chat_history:
    st.markdown("---")
    for speaker, msg in reversed(st.session_state.chat_history):
        st.markdown(f"**{speaker}:** {msg}")
