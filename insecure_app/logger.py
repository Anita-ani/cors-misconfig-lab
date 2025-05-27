import logging

logging.basicConfig(
    filename="access.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_access(origin: str, outcome: str, app: str):
    logging.info(f"[{app}] Origin: {origin} | Result: {outcome}")
