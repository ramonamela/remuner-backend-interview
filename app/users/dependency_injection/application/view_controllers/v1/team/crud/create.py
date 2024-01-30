from dependency_injector import containers, providers

from app.users.application.view_controllers.v1.team.v1.common.input_mapping_service import (
    TeamCrudPostInputMappingServiceV1,
)
from app.users.application.view_controllers.v1.team.v1.crud.create import CreateTeamViewControllerV1
from app.users.dependency_injection.infrastructure.persistence.team_bo import (
    TeamBOPersistenceServices,
)


class CreateTeamViewControllers(containers.DeclarativeContainer):

    v1 = providers.Singleton(
        CreateTeamViewControllerV1,
        input_mapping_service=TeamCrudPostInputMappingServiceV1(),
        team_bo_persistence_service=TeamBOPersistenceServices.tortoise,
    )
