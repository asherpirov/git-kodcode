from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel

from day1.db_mangment import *
from day2.db import *
from day3.queries import *
from day4.reports import *
class NewSoldier(BaseModel):
    name : str
    rank : str
    unit : str

class UpdateSoldier(BaseModel):
    rank : str
    unit : str

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

@app.get("/soldiers/search")
def search(name:str):
    return get_name(name)

@app.get("/soldiers/units")
def get_all_units():
    return get_all_unit()

@app.get("/soldiers/missing-rank")
def get_missing_rank():
    return missing_rank()

@app.get("/stats/summary")
def get_all_summary():
    return get_summary()

@app.get("/stats/units")
def get_unit():
    return count_by_unit()

@app.get("/stats/understaffed")
def get_unit_with_multiple():
    return get_units_with_multiple_soldiers()

@app.get("/soldiers/{id}")
def get_soldier(id: int):
    soldier = get_by_id(id)
    if not soldier:
        raise HTTPException(status_code=404, detail="not found")
    return soldier

@app.post("/soldiers", status_code=201)
def add_soldier(data:NewSoldier):
    return create(**data.model_dump())

@app.put("/soldiers/{id}")
def update_soldier(id: int, data:UpdateSoldier):
    has_update = update(id, data.model_dump())
    if not has_update:
        raise HTTPException(status_code=404, detail="not found")
    return has_update

@app.delete("/soldiers/{id}")
def delete_soldier(id: int):
    deleted = delete(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="not found")


if __name__ == "__main__":
    uvicorn.run(app)