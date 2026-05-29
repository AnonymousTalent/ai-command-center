from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

@app.get("/")
def root():
    return {
        "status": "AI Command Center Running",
        "api_key_loaded": bool(OPENAI_API_KEY)
    }