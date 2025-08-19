from fastapi import APIRouter, HTTPException
from app.services.rag_service import rag_chain
from app.schemas import AskRequest, RAGResponse

app = APIRouter()

@app.post("/rag/ask", response_model=RAGResponse)
async def ask_question(query:AskRequest):
    """
    Endpoint to ask a question using the RAG chain.
    """
    try:      
        answer = rag_chain.invoke({"question": query.question})     
        return RAGResponse(question=query.question,answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))