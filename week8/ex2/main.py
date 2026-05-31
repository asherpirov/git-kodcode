from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"service": "my-api", "version": "1.0"}

@app.get("/users/admin")
def get_admin():
  return {"role": "admin", "access": "full"}

@app.get("/users/{user_id}")
def user(user_id):
    return {"user_id": user_id
        ,"name":  f"User_{user_id}",
            "email": f"User_{user_id}@example.com"}





