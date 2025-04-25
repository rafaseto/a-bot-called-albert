from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .chain import chain

class QueryRequest(BaseModel):
    text: str

class QueryResponse(BaseModel):
    summary: str

app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.post("/query", response_model=QueryResponse)
async def query(request: QueryRequest):
    try:
        result = chain.invoke(input=request.text)
        return {"summary": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))