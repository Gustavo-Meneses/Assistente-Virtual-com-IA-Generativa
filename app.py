import streamlit as st

from utils.loader import load_knowledge_base
from core.memory import ConversationMemory
from core.rag import SimpleRAG
from core.llm import generate_response

# =============================
# CONFIGURAÇÃO DA PÁGINA
# =============================
st.set_page_config(
    page_title="Assistente IA",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Assistente Virtual com IA Generativa")

# =============================
# ESTADO DA SESSÃO
# =============================
if "memory" not in st.session_state:
    st.session_state.memory = ConversationMemory()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "rag" not in st.session_state:
    kb = load_knowledge_base("data/base_conhecimento.txt")
    st.session_state.rag = SimpleRAG(kb)

# =============================
# INPUT DO USUÁRIO
# =============================
user_input = st.chat_input("Digite sua pergunta...")

if user_input:
    # Recuperar contexto (RAG)
    context = st.session_state.rag.retrieve(user_input)

    # Histórico
    history = st.session_state.memory.get_context()

    # Gerar resposta
    with st.spinner("Pensando..."):
        response = generate_response(user_input, context, history)

    # Salvar memória
    st.session_state.memory.add(user_input, response)

    # Salvar chat
    st.session_state.chat_history.append(("user", user_input))
    st.session_state.chat_history.append(("assistant", response))

# =============================
# EXIBIÇÃO DO CHAT
# =============================
for role, message in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(message)
