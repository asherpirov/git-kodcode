from fastapi import FastAPI

app = FastAPI()

@app.get("/calc/{a}/{op}/{b}")
def calc(a, op, b):
    result = None
    if op == "div":
        if b == "0":
            return {"Zero Division Error"}
        result = float(a) / float(b)
    elif op == "add":
        result =  float(a) + float(b)
    elif op == "sub":
        result = float(a) - float(b)
    elif op == "mul":
        result = float(a) * float(b)

    return {"operation": op, "result": result}



