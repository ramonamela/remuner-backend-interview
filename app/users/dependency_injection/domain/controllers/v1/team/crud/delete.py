from dependency_injector import containers, providers

from app.users.dependency_injection.persistence.team_bo import (
    TeamBOPersistenceServices,
)
from app.users.domain.controllers.v1.team.crud.delete import DeleteTeamControllerV1


class DeleteTeamControllers(containers.DeclarativeContainer):

    v1 = providers.Singleton(
        DeleteTeamControllerV1,
        team_bo_persistence_service=TeamBOPersistenceServices.remuner,
    )
