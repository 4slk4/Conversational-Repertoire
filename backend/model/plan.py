from pydantic import BaseModel

class Plan(BaseModel):
    name: str
    content: str