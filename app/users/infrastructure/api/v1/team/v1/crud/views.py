from typing import List

from fastapi import HTTPException

from app.users.dependency_injection.application.view_controllers.v1.team.crud.create import (
    CreateTeamViewControllers,
)
from app.users.dependency_injection.application.view_controllers.v1.team.crud.get import (
    GetTeamViewControllers,
)
from app.users.infrastructure.api.v1.team.v1.crud.view_models import (
    TeamCrudIdOutputV1,
    TeamCrudInputV1,
)
from app.users.infrastructure.persistence.exceptions.team_bo import RepeatedTeamNameException


async def teams_get_v1() -> List[TeamCrudIdOutputV1]:
    view_controller = GetTeamViewControllers.v1()
    return await view_controller()


async def teams__team_id_get_v1(team_id: int) -> TeamCrudIdOutputV1:
    view_controller = GetTeamViewControllers.v1()
    return await view_controller(team_id=team_id)


async def teams_post_v1(post_input: TeamCrudInputV1) -> TeamCrudIdOutputV1:
    view_controller = CreateTeamViewControllers.v1()
    try:
        return await view_controller(input_team=post_input)
    except RepeatedTeamNameException:
        raise HTTPException(status_code=409, detail="Team name already exists in the database")


async def teams__team_id_post_v1(post_input: TeamCrudInputV1) -> TeamCrudIdOutputV1:
    return TeamCrudIdOutputV1(**{"id": 1})


async def teams__team_id_delete_v1(post_input: TeamCrudInputV1) -> TeamCrudIdOutputV1:
    return TeamCrudIdOutputV1(**{"id": 1})
