import json
import logging
import os

from fastapi import FastAPI

APP_ENV = os.environ.get("APP_ENV", "development")
PORT = int(os.environ.get("PORT", "8000"))


class JsonFormatter(logging.Formatter):
    def format(self, record):
        payload = {
            "timestamp": self.formatTime(record, "%Y-%m-%dT%H:%M:%S"),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }
        return json.dumps(payload)


handler = logging.StreamHandler()
handler.setFormatter(JsonFormatter())
logging.basicConfig(
    level=os.environ.get("LOG_LEVEL", "INFO").upper(),
    handlers=[handler],
)
logger = logging.getLogger("my_dockerized_app")

app = FastAPI(title="my_dockerized_app")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/info")
def info():
    logger.info("info endpoint requested")
    return {"app_env": APP_ENV, "cwd": os.getcwd()}


if __name__ == "__main__":
    import uvicorn

    logger.info("starting server on port %s (app_env=%s)", PORT, APP_ENV)
    # Binding to all interfaces is required so the service is reachable
    # from outside the container; nosec covers bandit's B104 false positive.
    uvicorn.run(app, host="0.0.0.0", port=PORT)  # nosec B104
