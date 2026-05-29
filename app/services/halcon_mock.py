import random
import uuid
from datetime import datetime

def generate_defect_inspection():
    """模擬HALCON回傳的缺陷檢測資料"""
    defect_types = ["solder_bridge", "missing_component", "misalignment", "void", "scratch"]
    return {
        "inspection_id": str(uuid.uuid4())[:8],
        "timestamp": datetime.now().isoformat(),
        "defects": [
            {
                "type": random.choice(defect_types),
                "x": random.randint(10, 100),
                "y": random.randint(10, 100),
                "area_mm2": round(random.uniform(0.1, 5.0), 2),
                "confidence": round(random.uniform(0.7, 0.99), 2)
            }
            for _ in range(random.randint(1, 4))
        ],
        "total_components": random.randint(100, 500),
        "pass_fail": random.choice(["PASS", "FAIL"])
    }