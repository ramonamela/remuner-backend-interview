from dependency_injector import containers, providers

from app.users.dependency_injection.persistence.team_bo import (
    TeamBOPersistenceServices,
)
from app.users.domain.controllers.v1.team.crud.create import CreateTeamControllerV1


class CreateTeamControllers(containers.DeclarativeContainer):

    v1 = providers.Singleton(
        CreateTeamControllerV1,
        team_bo_persistence_service=TeamBOPersistenceServices.remuner,
    )
