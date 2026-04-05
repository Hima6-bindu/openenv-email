from pydantic import BaseModel

class Observation(BaseModel):
    email_text: str
    sender: str

class Action(BaseModel):
    action_type: str   # classify / extract / reply
    value: str

class Reward(BaseModel):
    score: float