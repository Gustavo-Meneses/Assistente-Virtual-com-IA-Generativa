from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
import streamlit as st

client = MistralClient(api_key=st.secrets["MISTRAL_API_KEY"])

def generate_response(prompt):
    response = client.chat(
        model="mistral-small",
        messages=[ChatMessage(role="user", content=prompt)]
    )
    
    return response.choices[0].message.content
