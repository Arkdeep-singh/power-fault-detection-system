from fastapi import FastAPI

app = FastAPI(
    title="Power Fault Detection System",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Power Fault Detection System API is running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }