from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.routes import router  # <-- Make sure this import matches your file/module name

app = FastAPI(title="FastAPI Sample Skeleton")

origins = [
    "http://localhost:3000",
    "http://34.227.90.56",
    "http://3.89.103.234",
    "http://44.204.194.121",
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
# sudo systemctl restart fastapi # Restart the FastAPI service
# sudo systemctl status fastapi # Check the status of the FastAPI service
# sudo journalctl -u fastapi -f # View the logs for the FastAPI service
# sudo nginx -t # Test the Nginx configuration
