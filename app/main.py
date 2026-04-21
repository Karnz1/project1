from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health_check():
    return "insert health check logic"

@app.get("/ready")
def dep_ready():
    return "dependencies check"

@app.get("/metrics")
def get_metrics():
    return "return prometheus metrics"





