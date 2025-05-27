from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from logger import log_access

app = FastAPI(title="CORS Replay – Insecure Version")

# Insecure: allow all origins, headers, methods
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # wild open
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/sensitive-data")
def get_sensitive_data():
    log_access("*", "Allowed (insecure)", "insecure")
    return {"credit_card": "4111-xxxx-xxxx-1234", "ssn": "123-45-6789"}
