import json
from app.utils.ai_clients import call_openai  # 沿用你已有的

SYSTEM_PROMPT = """你是工業AI專家。根據HALCON檢測到的缺陷資料，分析可能原因並給出製程調整建議。
回傳JSON格式：
{
  "root_cause": "簡短原因",
  "process_parameters": ["建議調整1", "建議調整2"],
  "confidence_score": 0.0~1.0,
  "readable_report": "給產線工程師的自然語言報告"
}"""

def analyze_defects(defect_data: dict) -> dict:
    user_prompt = f"""檢測結果如下：
缺陷列表：{json.dumps(defect_data['defects'], indent=2)}
總零件數：{defect_data['total_components']}
最終結果：{defect_data['pass_fail']}

請分析可能原因並給出製程調整建議。"""
    
    response = call_openai(
        prompt=user_prompt,
        model="gpt-4o-mini",
        system=SYSTEM_PROMPT,
        temperature=0.3
    )
    # 嘗試解析JSON，若失敗則回傳原始文字
    try:
        return json.loads(response)
    except:
        return {"readable_report": response, "confidence_score": 0.5}