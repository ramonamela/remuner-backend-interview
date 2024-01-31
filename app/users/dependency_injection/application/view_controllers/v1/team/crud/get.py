from dependency_injector import containers, providers

from app.users.application.view_controllers.v1.team.v1.common.output_mapping_service import (
    TeamCrudOutputMappingServiceV1,
)
from app.users.application.view_controllers.v1.team.v1.crud.get import GetTeamViewControllerV1
from app.users.dependency_injection.infrastructure.persistence.team_bo import (
    TeamBOPersistenceServices,
)


class GetTeamViewControllers(containers.DeclarativeContainer):

    v1 = providers.Singleton(
        GetTeamViewControllerV1,
        output_mapping_service=TeamCrudOutputMappingServiceV1(),
        team_bo_persistence_service=TeamBOPersistenceServices.remuner,
    )
