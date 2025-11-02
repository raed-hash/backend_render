from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse, Response
import os
from app.routers import auth

app = FastAPI(
    title="EsetX API",
    docs_url="/docs",             # garante docs
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

# CORS
CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*")
origins = [o.strip() for o in CORS_ORIGINS.split(",")] if CORS_ORIGINS else ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins if origins != ["*"] else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# >>> NOVO: raiz redireciona para /docs
@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")

# >>> NOVO: favicon "vazio" (evita 404 no favicon)
@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return Response(status_code=204)

# healthcheck
@app.get("/healthz")
def healthz():
    return {"ok": True}

# rotas de auth
app.include_router(auth.router)
