from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..agents import route_to_agent

router = APIRouter()

class ChatRequest(BaseModel):
    agent_name: str
    prompt: str

@router.post("/chat")
def chat(req: ChatRequest):
    result = route_to_agent(req.agent_name, req.prompt)
    return result