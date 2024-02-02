from dependency_injector import containers, providers

from app.users.dependency_injection.persistence.team_bo import TeamBOPersistenceServices
from app.users.domain.controllers.v1.team.utilities.stats import GetTeamsStatsControllerV1


class GetTeamsStatsControllers(containers.DeclarativeContainer):

    v1 = providers.Singleton(
        GetTeamsStatsControllerV1,
        team_bo_persistence_service=TeamBOPersistenceServices.remuner,
    )
