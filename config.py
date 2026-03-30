import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

def get_mistral_key():
    if "MISTRAL_API_KEY" in st.secrets:
        return st.secrets["MISTRAL_API_KEY"]
    return os.getenv("MISTRAL_API_KEY")

MISTRAL_API_KEY = get_mistral_key()

MODEL_NAME = "mistral-small-latest"
