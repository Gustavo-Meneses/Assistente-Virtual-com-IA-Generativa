from openai import OpenAI
import streamlit as st

# pega chave do mistral
api_key = st.secrets["MISTRAL_API_KEY"]

client = OpenAI(
    api_key=api_key,
    base_url="https://api.mistral.ai/v1"
)

MODEL_NAME = "mistral-small-latest"

SYSTEM_PROMPT = """
Você é um assistente virtual inteligente.
"""

def generate_response(user_input, context="", memory=""):
    try:
        prompt = f"""
Contexto:
{context}

Histórico:
{memory}

Pergunta:
{user_input}

Resposta:
"""

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"❌ Erro: {str(e)}"
