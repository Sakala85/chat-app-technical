from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from services import process_message
from utils import validate_chat_history

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserMessage(BaseModel):
    chat_history: List[dict]
    message: str

@app.post("/chat")
async def chat_endpoint(payload: UserMessage):
    # Validate chat history
    if not validate_chat_history(payload.chat_history):
        raise HTTPException(status_code=400, detail="Invalid chat history")

    # Process and return the agent's response
    agent_response = await process_message(payload.message)
    return {"reply": agent_response}
