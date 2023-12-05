from pydantic import BaseModel

class Target(BaseModel):
    goal: str
    situation: str
    occupation: str
    relationship: str
    activity: str
    