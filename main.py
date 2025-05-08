from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

# 定義輸入資料格式
class Operation(BaseModel):
    a: float
    b: float

@app.get("/")
def read_root():
    return {"message": "這是計算機 API 💫"}

@app.post("/add")
def add(data: Operation):
    return {"result": data.a + data.b}

@app.post("/subtract")
def subtract(data: Operation):
    return {"result": data.a - data.b}

@app.post("/multiply")
def multiply(data: Operation):
    return {"result": data.a * data.b}

@app.post("/divide")
def divide(data: Operation):
    if data.b == 0:
        return {"error": "不能除以零"}
    return {"result": data.a / data.b}





class PowerInput(BaseModel):
    base: float
    exponent: float

@app.post("/power")
def power(data: Operation):
    return {"result": data.a ** data.b}
