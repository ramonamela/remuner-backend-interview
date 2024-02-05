import pytest
from factory import Factory

from app.users.dependency_injection.persistence.team_bo import TeamBOPersistenceServices
from app.users.domain.bo.team_bo import TeamBO


class TeamBOFactory(Factory):

    class Meta:
        model = TeamBO

    name = "RemunerTeam"
    user_ids = []
    users = None


@pytest.fixture
async def team_bo_factory_db():
    persistence_service = TeamBOPersistenceServices.remuner()
    team_bo = TeamBOFactory()
    await persistence_service.create(team_bo)
    return team_bo
