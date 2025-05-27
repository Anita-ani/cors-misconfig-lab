# CORS Misconfiguration Replay Lab

This project simulates a common web API vulnerability: misconfigured Cross-Origin Resource Sharing (CORS). It includes both insecure and secure versions to demonstrate exploitation and proper mitigation.

## 🔓 Insecure App

- Allows any origin via `Access-Control-Allow-Origin: *`
- Exposes sensitive data to any frontend
- Simulated with a basic `public.html`

## 🛡️ Secure App

- Only allows trusted domains via `Access-Control-Allow-Origin`
- Blocks untrusted cross-origin attempts
- Logs access origin headers

## 📂 Structure

- `insecure_app/` – vulnerable to CORS exploitation
- `secure_app/` – protected using FastAPI CORS middleware
- `public.html` – simulated frontend attack/demo page

## ▶️ How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt

2. Start the APIs
cd insecure_app
uvicorn main:app --reload --port 8030

cd ../secure_app
uvicorn main:app --reload --port 8031

3. Serve public.html
cd insecure_app
python -m http.server 5500
# then open http://localhost:5500/public.html

-Use Case
This lab is ideal for security awareness training, CORS debugging, and workshops
 on web application attack surfaces.


For Educational Use Only
