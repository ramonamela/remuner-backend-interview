from pydantic import BaseModel


class UserCrudPostInputV2(BaseModel):
    name: str


class UserCrudPostOutputV2(BaseModel):
    id: int
