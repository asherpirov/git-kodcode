from fastapi import FastAPI

app = FastAPI()

@app.get("/greet")
def greet(name: str = "world"):
    return {"message": f"Hello, {name}!"}




