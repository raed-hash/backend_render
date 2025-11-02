from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from app.routers import auth

app = FastAPI(title="EsetX API")

CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*")
origins = [o.strip() for o in CORS_ORIGINS.split(",")] if CORS_ORIGINS else ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins if origins != ["*"] else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/healthz")
def healthz():
    return {"ok": True}

app.include_router(auth.router)
