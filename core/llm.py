from mistralai import Mistral
from config import MISTRAL_API_KEY, MODEL_NAME

if not MISTRAL_API_KEY:
    raise ValueError("❌ MISTRAL_API_KEY não encontrada.")

client = Mistral(api_key=MISTRAL_API_KEY)

SYSTEM_PROMPT = """
Você é um assistente virtual inteligente.

Regras:
- Seja claro e objetivo
- Use o contexto fornecido
- Se não souber, diga que não tem certeza
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

        response = client.chat.complete(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"❌ Erro: {str(e)}"
