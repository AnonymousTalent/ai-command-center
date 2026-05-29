from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from .auth import verify_jwt
from .routers import chat, agents

app = FastAPI(title="AI Command Center", version="0.1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router, prefix="/api/v1", dependencies=[Depends(verify_jwt)])
app.include_router(agents.router, prefix="/api/v1", dependencies=[Depends(verify_jwt)])

@app.get("/health")
def health():
    return {"status": "ok"}