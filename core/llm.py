from openai import OpenAI
from config import OPENAI_API_KEY, MODEL_NAME

client = OpenAI(api_key=OPENAI_API_KEY)

SYSTEM_PROMPT = """
Você é um assistente virtual inteligente.

Regras:
- Seja claro e objetivo
- Use o contexto fornecido
- Se não souber, diga que não tem certeza
"""


def generate_response(user_input, context="", memory=""):
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
