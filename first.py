from fastapi import FastAPI
from enum import Enum

class ModelName(str, Enum):
    alxenet = "alxenet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/")
async def root():
    return {"meassage":"Hello World"}

'''
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}
순서 문제 주의하기!
'''
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alxenet:
        return {"model_name": model_name,"message": "Deep Learning FTW!"}

    if mode_name.value == "lenet":
        return {"model_name": model_name, "message":"LeCNN all the images"}

    return {"model_name": model_name, "message":"Have some residuals"}        
