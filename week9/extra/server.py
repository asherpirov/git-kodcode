from fastapi import FastAPI
import uvicorn
import mysql.connector

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run()
