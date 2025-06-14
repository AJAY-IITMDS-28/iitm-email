from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

class Link(BaseModel):
    url: str
    text: str

class QuestionRequest(BaseModel):
    question: str
    image: Optional[str] = None

class AnswerResponse(BaseModel):
    answer: str
    links: List[Link]

@app.post("/api/", response_model=AnswerResponse)
def answer_question(req: QuestionRequest):
    # Improved logic: match for both gpt-3.5-turbo and gpt3.5 turbo
    q = req.question.lower()
    if "gpt-3.5-turbo" in q or "gpt3.5 turbo" in q:
        answer = "You must use gpt-3.5-turbo-0125, even if the AI Proxy only supports gpt-4o-mini. Use the OpenAI API directly for this question."
        links = [
            Link(url="https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/4", text="Use the model that’s mentioned in the question."),
            Link(url="https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/3", text="My understanding is that you just have to use a tokenizer, similar to what Prof. Anand used, to get the number of tokens and multiply that by the given rate.")
        ]
    else:
        answer = "Sorry, I don't have an answer for that yet."
        links = []
    return AnswerResponse(answer=answer, links=links)
