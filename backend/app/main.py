from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from backend.app.routes.content_routes import router

app = FastAPI(
    title="YouTube AI Chatbot",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Routes
app.include_router(router)

# Serve Frontend
app.mount(
    "/",
    StaticFiles(directory="frontend", html=True),
    name="frontend"
)