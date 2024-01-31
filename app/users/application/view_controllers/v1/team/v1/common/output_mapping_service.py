from app.users.domain.bo.team_bo import TeamBO
from app.users.domain.bo.user_bo import UserBO
from app.users.infrastructure.api.v1.team.v1.crud.view_models import (
    TeamCrudOutputV1,
    TeamCrudUserOutputV1,
)


class TeamCrudOutputMappingServiceV1:

    def _get_user(self, user_bo: UserBO) -> TeamCrudUserOutputV1:
        return TeamCrudUserOutputV1(
            id=user_bo.id,
            first_name=user_bo.first_name,
            last_name=user_bo.last_name,
            email=user_bo.email,
        )

    def __call__(self, team_bo: TeamBO) -> TeamCrudOutputV1:
        return TeamCrudOutputV1(
            id=team_bo.id,
            name=team_bo.name,
            users=[self._get_user(user) for user in team_bo.users],
        )
