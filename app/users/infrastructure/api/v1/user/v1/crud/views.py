from pydantic import BaseModel


class PostInputV1(BaseModel):
    name: str


class PostInputV2(BaseModel):
    first_name: str


async def users_post_v1(post_input: PostInputV1):
    return {"message": "Users post v1"}


async def users_post_v2(post_input: PostInputV2):
    return {"message": "Users post v2"}
