# from typing import Optional
import unlock
from fastapi import FastAPI
from pydantic import BaseModel


# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}

class Command(BaseModel):
    arg1: str

app = FastAPI()

@app.post("/6699")
def callUnlock(command : Command):
    print(command.arg1)
    unlock.run(command.arg1)
    return {0}

@app.post("/")
def back():
    return 111