from sentence_transformers import SentenceTransformer
import faiss
import glob
import yaml


class GetContext:
    def __init__(self, model="all-MiniLM-L6-v2", context_pattern="../docs/*.yaml"):
        self.model = SentenceTransformer(model)
        self.context_files = glob.glob(context_pattern)
        self.index = faiss.IndexFlatL2(384)
        self.texts = []
        self.read_context()

    def read_context(self):
        for file in self.context_files:
            with open(file, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
                content = yaml.dump(data)
                self.texts.append(content)
                emb = self.model.encode([content])
                self.index.add(emb)

    def get_context(self, query: str, top_k: int = 3):
        if self.index.ntotal == 0:
            raise ValueError("Nenhum documento YAML carregado no RAG.")

        query_emb = self.model.encode([query])
        D, I = self.index.search(query_emb, top_k)

        results = []
        for idx in I[0]:
            if 0 <= idx < len(self.texts):
                results.append(self.texts[idx])

        if not results:
            raise ValueError("Nenhum contexto encontrado.")

        return "\n-------\n".join(results)
