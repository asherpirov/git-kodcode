from fastapi import FastAPI
import uvicorn
from db_mangment import *

app = FastAPI()

@app.post("/setup")
def setup_():
    setup()

@app.get("/schema")
def get_schema_():
    return get_schema()

@app.get("/soldiers")
def get_all_soldiers_():
    return get_soldiers()

if __name__ == "__main__":
    uvicorn.run(app)
