from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import routes

app = FastAPI(title="FastAPI Sample Skeleton")

app.include_router(routes.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://3.89.103.234/api/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
