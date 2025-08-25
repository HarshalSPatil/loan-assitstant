from fastapi import APIRouter
from pydantic import BaseModel
from rag_pipeline.answer import answer

router = APIRouter()

class Query(BaseModel):
    query: str

class Response(BaseModel):
    answer: str

@router.post("/chat", response_model=Response)
def chat(q: Query):
    a = answer(q.query)
    return Response(answer=a)

@router.get("/health")
def health():
    return {"status": "ok"}