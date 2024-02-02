from typing import List

from fastapi import HTTPException

from app.users.api.v1.team.v1.common.input_mapping_service import TeamCrudInputMappingServiceV1
from app.users.api.v1.team.v1.common.view_models import TeamIdOutputV1, TeamInputV1
from app.users.api.v1.team.v1.crud.output_mapping_service import TeamCrudOutputMappingServiceV1
from app.users.api.v1.team.v1.crud.view_models import (
    TeamCrudOutputV1,
)
from app.users.dependency_injection.domain.controllers.v1.team.crud.create import (
    CreateTeamViewControllers,
)
from app.users.dependency_injection.domain.controllers.v1.team.crud.delete import (
    DeleteTeamViewControllers,
)
from app.users.dependency_injection.domain.controllers.v1.team.crud.get import (
    GetTeamViewControllers,
)
from app.users.dependency_injection.domain.controllers.v1.team.crud.update import (
    UpdateTeamViewControllers,
)
from app.users.domain.persistence.exceptions.team_bo import (
    RepeatedTeamNameException,
    TeamNotFoundException,
)


async def teams_get_v1() -> List[TeamCrudOutputV1]:
    view_controller = GetTeamViewControllers.v1()
    output_mapping_service = TeamCrudOutputMappingServiceV1()
    return [output_mapping_service(team_bo=team_bo) for team_bo in await view_controller()]


async def teams__team_id_get_v1(team_id: int) -> TeamCrudOutputV1:
    view_controller = GetTeamViewControllers.v1()
    output_mapping_service = TeamCrudOutputMappingServiceV1()
    return output_mapping_service(team_bo=await view_controller(team_id=team_id))


async def teams_post_v1(post_input: TeamInputV1) -> TeamIdOutputV1:
    view_controller = CreateTeamViewControllers.v1()
    input_mapping_service = TeamCrudInputMappingServiceV1()
    try:
        return TeamIdOutputV1(
            id=await view_controller(input_team=input_mapping_service(post_input))
        )
    except RepeatedTeamNameException:
        raise HTTPException(status_code=409, detail="Team name already exists in the database")


async def teams__team_id_post_v1(team_id: int, post_input: TeamInputV1) -> TeamIdOutputV1:
    view_controller = UpdateTeamViewControllers.v1()
    input_mapping_service = TeamCrudInputMappingServiceV1()
    try:
        return TeamIdOutputV1(
            id=await view_controller(team_id=team_id, input_team=input_mapping_service(post_input))
        )
    except TeamNotFoundException:
        raise HTTPException(status_code=404, detail="Team not found")


async def teams__team_id_delete_v1(team_id: int):
    view_controller = DeleteTeamViewControllers.v1()
    try:
        await view_controller(team_id=team_id)
        return {}
    except TeamNotFoundException:
        raise HTTPException(status_code=404, detail="Team not found")
