from app.integrations.domain.bo.integration_bo import IntegrationBO
from app.users.api.v1.user.v1.common.view_models import (
    UserIntegrationOutputV1,
    UserOutputV1,
    UserTeamOutputV1,
)
from app.users.domain.bo.team_bo import TeamBO
from app.users.domain.bo.user_bo import UserBO


class UserOutputMappingServiceV1:

    def _get_team(self, team_bo: TeamBO) -> UserTeamOutputV1:
        return UserTeamOutputV1(
            id=team_bo.id,
            name=team_bo.name,
        )

    def _get_integration(self, integration_bo: IntegrationBO) -> UserIntegrationOutputV1:
        return UserIntegrationOutputV1(
            id=integration_bo.id,
            name=integration_bo.name,
            status=integration_bo.status,
        )

    def __call__(self, user_bo: UserBO) -> UserOutputV1:
        return UserOutputV1(
            id=user_bo.id,
            first_name=user_bo.first_name,
            last_name=user_bo.last_name,
            email=user_bo.email,
            status=user_bo.status,
            teams=[self._get_team(team) for team in user_bo.teams],
            integrations=[
                self._get_integration(integration) for integration in user_bo.integrations
            ],
        )
