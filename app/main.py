from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import routes

app = FastAPI(title="FastAPI Sample Skeleton")

app.include_router(routes.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://3.89.103.234",
        "http://http://54.165.61.74/",
        "http://my-react-app-demo-july-18-2025.s3-website-us-east-1.amazonaws.com",
        "https://d2tvxnyll1ff8k.cloudfront.net"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

