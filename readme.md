# Chatbort

### Tecnologias usadas:

- Python, base do codigo backend (futuramente pretendo colocar Rust para orquestração da Ram e da vram)
- FastAPI, API de desenvolvimento web
- Faiss, busca vetorial
- Yaml, base de conhecimento usando markdown
- Sentence Transformers, para gerar embeddings
- N8N, para automatizar processos

### Pré requesitos:

Python 3.10 +
PIP ou UV

Ollama
```
ollama pull qwen2.5-coder:1.5b-base
```
PS: caso queira alterar o modelo basta alterar o script config.py na linha 2

### Criar ambiente e instalação de denpendencias:

Usando UV:

```
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

### Rodando A API

Dentro do diretorio do rag_api:

```
uvicorn main:app --reload --port 8000
```

Testar o endpoint:

```
http://127.0.0.1:8000/docs/
```

### Futuras melhorias

- Normalização do idioma para o ingles
- TTS de resposta para o chatbot
- Introduzir arquitetura com Docker
