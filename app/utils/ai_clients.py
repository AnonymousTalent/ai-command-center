import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY", "fake-key"))

def call_openai(prompt: str, model: str = "gpt-3.5-turbo") -> str:
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"OpenAI error: {str(e)}"

def call_deepseek_mock(prompt: str) -> str:
    # 模擬 DeepSeek 回應，之後換真實 API
    return f"[DeepSeek Mock] 收到：{prompt[:50]}..."