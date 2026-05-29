from fastapi import APIRouter
from ..agents import AGENTS

router = APIRouter()

@router.get("/agents")
def list_agents():
    return AGENTS