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
from .utils.email_client import send_application_email

def handle_job_application(company: str, job_title: str, job_description: str = "") -> dict:
    prompt = f"""
請根據以下公司與職缺，幫我產生一封專業且有說服力的中文求職信。
公司：{company}
職稱：{job_title}
職缺描述：{job_description}

請使用我提供的範本風格，強調我的機械背景 + AI Command Center 專案。
姓名：徐志曆
信箱：Wshao777opscenter@gmail.com
"""

    # 呼叫 LLM 生成信件
    response = call_openai(prompt, model="gpt-4o-mini")
    
    subject = f"[求職] {job_title} – 徐志曆（機械背景 + AI 系統整合）"
    
    return {
        "agent": "job_application",
        "company": company,
        "job_title": job_title,
        "generated_body": response,
        "subject": subject
    }