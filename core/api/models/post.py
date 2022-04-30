from pydantic import BaseModel, validator


class PostModel(BaseModel):
    userId: int
    id: int
    title: str
    body: str
