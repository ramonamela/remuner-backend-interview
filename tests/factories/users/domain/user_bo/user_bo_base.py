import pytest
from factory import Factory

from app.users.dependency_injection.persistence.user_bo import UserBOPersistenceServices
from app.users.domain.bo.user_bo import UserBO
from app.users.enums import UserStatus


class UserBOFactory(Factory):
    class Meta:
        model = UserBO

    first_name = "RemunerName"
    last_name = "RemunerLast"
    email = "remuner@remuner.com"
    status = UserStatus.ACTIVE
    team_ids = []
    teams = None
    integrations = None


@pytest.fixture
async def user_bo_factory_db():
    persistence_service = UserBOPersistenceServices.remuner()
    user_bo = UserBOFactory()
    await persistence_service.create(user_bo)
    return user_bo
