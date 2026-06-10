from fastapi import FastAPI, HTTPException
import uvicorn
from reports import get_summary, count_by_unit, get_units_with_multiple_soldiers
app = FastAPI()


@app.get("/stats/summary")
def get_all_summary():
    return get_summary()

@app.get("/stats/units")
def get_unit():
    return count_by_unit()

@app.get("/stats/understaffed")
def get_unit_with_multiple():
    return get_units_with_multiple_soldiers()


if __name__ == "__main__":
    uvicorn.run(app)