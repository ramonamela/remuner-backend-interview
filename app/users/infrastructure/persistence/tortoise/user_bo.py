from tortoise.exceptions import IntegrityError

from app.users.domain.bo.user_bo import UserBO
from app.users.domain.persistence.user_bo_persistence_interface import UserBOPersistenceInterface
from app.users.infrastructure.persistence.exceptions.user_bo import RepeatedEmailException
from app.users.models import User


class UserBOTortoisePersistenceService(UserBOPersistenceInterface):

    async def create(self, user_bo: UserBO):
        try:
            new_user = await User.create(
                first_name=user_bo.first_name,
                last_name=user_bo.last_name,
                email=user_bo.email,
                status=user_bo.status,
            )
        except IntegrityError as exc:
            if "duplicate key value violates unique constraint" in str(exc):
                raise RepeatedEmailException()
            raise exc
        user_bo.id = new_user.user_id
        return new_user.user_id
