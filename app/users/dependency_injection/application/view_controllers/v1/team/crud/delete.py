from dependency_injector import containers, providers

from app.users.application.view_controllers.v1.team.v1.crud.delete import DeleteTeamViewControllerV1
from app.users.dependency_injection.infrastructure.persistence.team_bo import (
    TeamBOPersistenceServices,
)


class DeleteTeamViewControllers(containers.DeclarativeContainer):

    v1 = providers.Singleton(
        DeleteTeamViewControllerV1,
        team_bo_persistence_service=TeamBOPersistenceServices.remuner,
    )
