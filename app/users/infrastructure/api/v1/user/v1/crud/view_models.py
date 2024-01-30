from pydantic import BaseModel


class UserCrudPostInputV1(BaseModel):
    first_name: str


class UserCrudPostOutputV1(BaseModel):
    id: int
