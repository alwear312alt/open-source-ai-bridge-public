
import os
import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Open Source AI Bridge")

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
MODEL = os.getenv("MODEL", "qwen2.5:3b")

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"status": "AI Bridge is ready"}

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        async with httpx.AsyncClient(timeout=120) as client:
            response = await client.post(
                f"{OLLAMA_URL}/api/generate",
                json={
                    "model": MODEL,
                    "prompt": request.message,
                    "stream": False
                }
            )
            response.raise_for_status()
            return {"reply": response.json()["response"]}
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e))
