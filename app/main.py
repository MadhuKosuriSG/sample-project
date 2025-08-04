from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.routes import router  # <-- Make sure this import matches your file/module name

app = FastAPI(title="FastAPI Sample Skeleton")

origins = [
    "http://localhost:3000",
    "http://34.227.90.56",
    "http://3.89.103.234",
    "http://dev-web-loadbalancer-891045896.us-east-1.elb.amazonaws.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
