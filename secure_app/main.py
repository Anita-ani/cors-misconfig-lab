from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from logger import log_access

app = FastAPI(title="CORS Replay – Secure Version")

# Only allow from trusted frontend
TRUSTED_ORIGINS = ["http://localhost:5500"]

# CORS policy (enforced by browser)
app.add_middleware(
    CORSMiddleware,
    allow_origins=TRUSTED_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/sensitive-data")
def get_sensitive_data(request: Request):
    origin = request.headers.get("origin")

    if origin not in TRUSTED_ORIGINS:
        log_access(origin or "unknown", "Blocked (untrusted origin)", "secure")
        raise HTTPException(status_code=403, detail="Forbidden: Untrusted origin")

    log_access(origin, "Allowed (secure)", "secure")
    return {"credit_card": "4111-xxxx-xxxx-1234", "ssn": "123-45-6789"}
