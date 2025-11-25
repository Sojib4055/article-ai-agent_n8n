from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr, HttpUrl
import uuid
import os
import httpx
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL")
if not N8N_WEBHOOK_URL:
    raise RuntimeError("N8N_WEBHOOK_URL is not set in .env file")

app = FastAPI(
    title="AI Article Agent Backend",
    description="Backend API that forwards requests to n8n workflow.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ProcessArticleRequest(BaseModel):
    email: EmailStr
    article_url: HttpUrl

class ProcessArticleResponse(BaseModel):
    session_id: str
    status: str
    n8n_status_code: int | None = None
    n8n_response: dict | None = None

@app.get("/")
async def root():
    return {"message": "AI Article Agent Backend is running"}

@app.post("/process-article", response_model=ProcessArticleResponse)
async def process_article(payload: ProcessArticleRequest):
    session_id = str(uuid.uuid4())

    data_to_n8n = {
        "email": payload.email,
        "article_url": str(payload.article_url),
        "session_id": session_id,
    }

    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            n8n_response = await client.post(
                N8N_WEBHOOK_URL,
                json=data_to_n8n,
            )
    except httpx.RequestError as e:
        raise HTTPException(
            status_code=502,
            detail=f"Failed to reach n8n webhook: {e}",
        )

    try:
        n8n_json = n8n_response.json()
    except Exception:
        n8n_json = None

    if n8n_response.status_code >= 400:
        raise HTTPException(
            status_code=502,
            detail={
                "message": "n8n returned an error",
                "n8n_status_code": n8n_response.status_code,
                "n8n_response": n8n_json,
            },
        )

    return ProcessArticleResponse(
        session_id=session_id,
        status="processing",
        n8n_status_code=n8n_response.status_code,
        n8n_response=n8n_json,
    )
