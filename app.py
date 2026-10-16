import os
import time
import httpx
from fastapi import FastAPI

TARGET_NAME = os.getenv("OPS_STATUS_TARGET_NAME", "example-service")
TARGET_URL = os.getenv("OPS_STATUS_TARGET_URL", "https://example.com/")

app = FastAPI(title="Ops Status")

@app.get("/")
def read_root():
    return {
        "service": "ops-status",
        "status": "running",
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
    }

@app.get("/checks")
def check_services():
    started = time.perf_counter()

    try:
        response = httpx.get(TARGET_URL, timeout=5.0)
        latency_ms = round((time.perf_counter() - started) * 1000, 1)

        return {
            "name": TARGET_NAME,
            "reachable": True,
            "status_code": response.status_code,
            "latency_ms": latency_ms,
        }

    except httpx.RequestError as error:
        latency_ms = round((time.perf_counter() - started) * 1000, 1)

        return {
            "name": TARGET_NAME,
            "reachable": False,
            "latency_ms": latency_ms,
            "error": str(error),
        }
