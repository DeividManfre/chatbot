from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from rag_engine import GetContext
from llm_client import RunLLM

app = FastAPI(title="Testing rag api", version="v1")
rag = GetContext()
llm = RunLLM()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

rag = GetContext()
llm = RunLLM()

@app.get("/api/v1/ask")
def ask(q: str):
    context = rag.get_context(q)
    
    prompt = f"""
    Use ONLY the context below to answer and answer in Brazilian Portuguese. 
    Do not use any other information.
    
    context:
    {context}
    
    question:
    {q}
    
    answer:
    
    """
    
    answer = llm.run_llm(prompt)
    return {"answer": answer, "status":"success"}