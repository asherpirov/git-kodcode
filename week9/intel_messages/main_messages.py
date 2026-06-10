from fastapi import FastAPI, HTTPException
import uvicorn
from queries import

app = FastAPI()


@app.get("/soldiers")
def get_rank(rank: str):
