from pydantic import BaseModel

class Assistance (BaseModel):
    topic: str
    description: str