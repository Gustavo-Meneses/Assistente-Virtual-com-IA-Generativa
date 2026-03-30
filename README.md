# 🤖 Assistente Virtual com IA Generativa

> Interface web com Streamlit, RAG e memória de conversa.

---

## 📌 Descrição

Assistente virtual com interface web moderna utilizando **Streamlit**, com suporte a **RAG** (Retrieval-Augmented Generation) para busca em base de conhecimento e **memória de conversa** persistente durante a sessão.

---

## 🚀 Tecnologias

| Tecnologia | Finalidade |
|---|---|
| Python | Linguagem principal |
| Streamlit | Interface web |
| OpenAI API | Modelo de linguagem |
| Scikit-learn (TF-IDF) | Busca por contexto (RAG) |

---

## ▶️ Como rodar

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```

### 2. Criar arquivo `.env`

```env
OPENAI_API_KEY=sua_chave_aqui
```

### 3. Executar a aplicação

```bash
streamlit run app.py
```

---

## 💡 Funcionalidades

- ✅ Interface estilo ChatGPT
- ✅ Memória de conversa
- ✅ Busca por contexto (RAG)
- ✅ Respostas inteligentes via OpenAI

---

## 🔥 Próximos passos

- [ ] Upload de PDF
- [ ] Banco vetorial com FAISS
- [ ] Deploy no Streamlit Cloud
- [ ] Autenticação de usuário

---

## 📦 Estrutura do projeto

```
.
├── app.py
├── requirements.txt
├── .env
└── README.md
```

---

## 📄 Licença

Este projeto está sob a licença MIT.
