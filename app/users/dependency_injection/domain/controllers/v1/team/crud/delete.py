from dependency_injector import containers, providers

from app.users.dependency_injection.persistence.team_bo import (
    TeamBOPersistenceServices,
)
from app.users.domain.controllers.v1.team.crud.delete import DeleteTeamViewControllerV1


class DeleteTeamViewControllers(containers.DeclarativeContainer):

    v1 = providers.Singleton(
        DeleteTeamViewControllerV1,
        team_bo_persistence_service=TeamBOPersistenceServices.remuner,
    )
