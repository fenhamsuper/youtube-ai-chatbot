from pydantic import BaseModel, Field

class ContentRequest(BaseModel):
    category: str = Field(..., example="horror")
    topic: str = Field(..., min_length=3)
    audience: str = Field(..., example="Teenagers")
    tone: str = Field(..., example="Engaging")
