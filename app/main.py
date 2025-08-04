from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.routes import router  # <-- Make sure this import matches your file/module name

app = FastAPI(title="FastAPI Sample Skeleton")

origins = [
    "http://localhost:3000",
    "http://34.227.90.56",
    "http://3.89.103.234"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
