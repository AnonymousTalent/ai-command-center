from typing import Dict, Any
from .utils.ai_clients import call_openai, call_deepseek_mock

AGENTS = {
    "reasoning": {
        "provider": "openai",
        "model": "gpt-4o-mini",
        "description": "邏輯推理與規劃"
    },
    "fast_batch": {
        "provider": "deepseek_mock",
        "model": "deepseek-chat",
        "description": "低成本批次回應"
    },
    "info": {
        "provider": "openai",
        "model": "gpt-3.5-turbo",
        "description": "快速資訊查詢"
    }
}

def route_to_agent(agent_name: str, prompt: str) -> Dict[str, Any]:
    agent = AGENTS.get(agent_name)
    if not agent:
        return {"error": f"Agent {agent_name} not found"}
    
    if agent["provider"] == "openai":
        response = call_openai(prompt, model=agent["model"])
    elif agent["provider"] == "deepseek_mock":
        response = call_deepseek_mock(prompt)
    else:
        response = "Unknown provider"
    
    return {
        "agent": agent_name,
        "provider": agent["provider"],
        "model": agent["model"],
        "response": response
    }
AGENTS = {
    # ... 你原本的 agents ...
    "job_application": {
        "provider": "openai",
        "model": "gpt-4o-mini",
        "description": "自動產生客製化求職信並寄送"
    },
    # ...
}