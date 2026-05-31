from datetime import datetime
from fastapi import FastAPI

app = FastAPI()

@app.get("/status")
def get_status():
    now = datetime.now()
    return {f"Asher_server: {now}"}

