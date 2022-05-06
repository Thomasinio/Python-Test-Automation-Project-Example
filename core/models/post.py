from pydantic import BaseModel


class PostModel(BaseModel):
    userId: int
    id: int
    title: str
    body: str
