import requests 
import json

from config import OLLAMA_URL , MODEL_NAME, LLM_SETTINGS



class RunLLM:
    def __init__(self, ollama_url=OLLAMA_URL, model_name=MODEL_NAME, llm_settings=LLM_SETTINGS):
        self.ollama_url = ollama_url
        self.model_name = model_name
        self.llm_settings = llm_settings
        
    def run_llm(self, prompt: str) -> str:
        payload = {
            "model": self.model_name,
            "prompt": prompt,
            **self.llm_settings
        }

        response = requests.post(self.ollama_url, json=payload)
        response.raise_for_status()
        
        data = response.text.split("\n")
        final_text = ""
        
        for line in data:
            if not line.strip():
                continue
            
            obj = json.loads(line)
            if "response" in obj:
                final_text += obj["response"]
                
        return final_text.strip()