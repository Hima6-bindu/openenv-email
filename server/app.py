from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ActionRequest(BaseModel):
    action: str = None

state = {"step": 0}

@app.post("/reset")
def reset():
    state["step"] = 0
    return {"message": "reset"}

@app.post("/step")
def step(req: ActionRequest):
    state["step"] += 1

    if state["step"] == 1:
        return {"observation": "Email detected", "reward": 1.0, "done": False}
    elif state["step"] == 2:
        return {"observation": "Marked important", "reward": 1.0, "done": False}
    else:
        return {"observation": "Replied", "reward": 1.0, "done": True}
