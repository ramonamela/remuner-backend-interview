import asyncio

from tortoise import transactions
from tortoise.exceptions import IntegrityError

from app.users.domain.bo.user_bo import UserBO
from app.users.domain.persistence.user_bo_persistence_interface import UserBOPersistenceInterface
from app.users.infrastructure.persistence.exceptions.team_bo import TeamNotFoundException
from app.users.infrastructure.persistence.exceptions.user_bo import RepeatedEmailException, UserNotFoundException
from app.users.models import Team, User


class UserBOTortoisePersistenceService(UserBOPersistenceInterface):

    @classmethod
    async def _add_to_user(cls, user, team_ids):
        teams = await Team.filter(team_id__in=team_ids).only("team_id")
        if len(teams) != len(team_ids):
            raise TeamNotFoundException()
        tasks = [user.teams.add(team) for team in teams]
        await asyncio.gather(*tasks)

    @transactions.atomic()
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
        if user_bo.team_ids is not None and len(user_bo.team_ids) > 0:
            await self._add_to_user(new_user, user_bo.team_ids)
        user_bo.id = new_user.user_id
        return new_user.user_id

    @classmethod
    def _generate_bo(cls, User):
        pass

    async def get_all(self):
        users = await User.all().prefetch_related("teams")
        raise Exception


    async def get(self, user_id: int):
        user = User.get(user_id=user_id).prefetch_related("teams")
        raise Exception

    async def delete(self, user_id: int):
        object_to_delete = await User.get(user_id=user_id)
        if object_to_delete:
            await object_to_delete.delete()
        else:
            raise UserNotFoundException()
