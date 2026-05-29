import streamlit as st
import requests
import json

st.set_page_config(page_title="AI Command Center - 工業AI中介層", layout="wide")
st.title("🏭 工業AI中介層展示平台")
st.markdown("HALCON模擬輸出 → AI分析 → 製程建議")

# 請用你實際的JWT token
JWT_TOKEN = "你的JWT"
API_URL = "http://localhost:8000/api/v1/industrial/inspect"

if st.button("執行產線檢測 (模擬)"):
    headers = {"Authorization": f"Bearer {JWT_TOKEN}"}
    resp = requests.post(API_URL, headers=headers)
    if resp.status_code == 200:
        data = resp.json()
        insp = data["inspection"]
        ana = data["analysis"]
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("📸 HALCON 檢測輸出")
            st.json(insp)
        with col2:
            st.subheader("🧠 AI 診斷與建議")
            if "readable_report" in ana:
                st.success(ana["readable_report"])
            if "process_parameters" in ana:
                st.info("🔧 建議調整參數：" + ", ".join(ana["process_parameters"]))
            st.metric("AI信心度", f"{ana.get('confidence_score',0):.0%}")
    else:
        st.error(f"API錯誤: {resp.status_code}")