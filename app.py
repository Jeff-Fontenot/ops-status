from fastapi import FastAPI

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
