from typing import Callable

from app.users.infrastructure.api.v1.user.v1.crud.view_models import (
    UserCrudPostInputV1,
    UserCrudPostOutputV1,
)


class CreateUserViewControllerV1:
    def __init__(self, input_mapping_service: Callable):
        pass

    def __call__(self, input_user: UserCrudPostInputV1):
        return UserCrudPostOutputV1(id=1)
