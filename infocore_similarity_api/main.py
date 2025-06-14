from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import numpy as np
import openai  # Requires `openai` library

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["OPTIONS", "POST"],
    allow_headers=["*"],
)

# Request body model
class SimilarityRequest(BaseModel):
    docs: List[str]
    query: str

@app.post("/similarity")
async def compute_similarity(data: SimilarityRequest):
    # Embed query and documents using OpenAI's embedding model
    model = "text-embedding-3-small"
    texts = [data.query] + data.docs
    embeddings = openai.embeddings.create(input=texts, model=model).data
    query_embedding = np.array(embeddings[0].embedding)
    doc_embeddings = [np.array(e.embedding) for e in embeddings[1:]]

    # Cosine similarity
    def cosine_sim(a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

    similarities = [cosine_sim(query_embedding, doc) for doc in doc_embeddings]
    top_indices = sorted(range(len(similarities)), key=lambda i: similarities[i], reverse=True)[:3]

    # Return top 3 matches
    return {"matches": [data.docs[i] for i in top_indices]}
