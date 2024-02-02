from app.users.domain.bo.user_bo import UserBO
from app.users.models import User


class UserBOMappingService:
    def __call__(self, user: User) -> UserBO:
        return UserBO(
            id=user.user_id,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            status=user.status,
        )
