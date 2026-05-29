from fastapi import APIRouter, Depends
from app.services.halcon_mock import generate_defect_inspection
from app.services.defect_analyzer import analyze_defects
from app.auth import verify_jwt

router = APIRouter()

@router.post("/industrial/inspect")
def run_inspection(user=Depends(verify_jwt)):
    # 1. 模擬HALCON檢測
    inspection = generate_defect_inspection()
    # 2. AI分析
    analysis = analyze_defects(inspection)
    return {
        "inspection": inspection,
        "analysis": analysis
    }