from dependency_injector import containers, providers

from app.users.dependency_injection.persistence.team_bo import (
    TeamBOPersistenceServices,
)
from app.users.domain.controllers.v1.team.crud.update import UpdateTeamControllerV1


class UpdateTeamControllers(containers.DeclarativeContainer):

    v1 = providers.Singleton(
        UpdateTeamControllerV1,
        team_bo_persistence_service=TeamBOPersistenceServices.remuner,
    )
