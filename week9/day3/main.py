from fastapi import FastAPI, HTTPException
import uvicorn
from queries import *
app = FastAPI()


@app.get("/soldiers")
def get_all_soldiers(rank: str | None = None, sort: str = None, unit: str = None):
    if rank is not None:
        return filter_by_rank(rank)
    elif sort is not None:
        return sort_soldiers(sort)
    elif unit is not None:
        return get_unit(unit)
    return []

@app.get("/soldiers/search")
def search(name:str):
    return get_name(name)

@app.get("/soldiers/units")
def get_all_units():
    return get_all_unit()

@app.get("/soldiers/missing-rank")
def get_missing_rank():
    return missing_rank()

if __name__ == "__main__":
    uvicorn.run(app)