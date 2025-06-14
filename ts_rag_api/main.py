from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from typing import Optional
import openai
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load TypeScript Book into memory (sample mock data for now)
docs = [
    {
        "excerpt": "`=>` is affectionately called the *fat arrow* in ES6.",
        "source": "https://github.com/basarat/typescript-book/blob/master/docs/arrow-functions.md"
    },
    {
        "excerpt": "`!!` is a trick to convert any value into an explicit boolean.",
        "source": "https://github.com/basarat/typescript-book/blob/master/docs/truthy.md"
    }
]

@app.get("/search")
async def search(q: Optional[str] = ""):
    query = q.lower()
    for doc in docs:
        if "fat arrow" in doc["excerpt"].lower() and "=>" in query:
            return {"answer": doc["excerpt"], "sources": doc["source"]}
        if "!!" in query or "boolean" in query:
            return {"answer": doc["excerpt"], "sources": doc["source"]}
    return {"answer": "No relevant excerpt found", "sources": ""}

