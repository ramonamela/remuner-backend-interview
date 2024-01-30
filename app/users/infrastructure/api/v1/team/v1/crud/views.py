from fastapi import HTTPException

from app.users.dependency_injection.application.view_controllers.v1.team.crud.create import (
    CreateTeamViewControllers,
)
from app.users.infrastructure.api.v1.team.v1.crud.view_models import (
    TeamCrudPostInputV1,
    TeamCrudPostOutputV1,
)
from app.users.infrastructure.persistence.exceptions.team_bo import RepeatedTeamNameException


async def teams_get_v1() -> TeamCrudPostOutputV1:
    return TeamCrudPostOutputV1(**{"id": 1})


async def teams__team_id_get_v1(team_id: int) -> TeamCrudPostOutputV1:
    return TeamCrudPostOutputV1(**{"id": 1})


async def teams_post_v1(post_input: TeamCrudPostInputV1) -> TeamCrudPostOutputV1:
    view_controller = CreateTeamViewControllers.v1()
    try:
        return await view_controller(input_team=post_input)
    except RepeatedTeamNameException:
        raise HTTPException(status_code=409, detail="Team name already exists in the database")


async def teams_post_v2(post_input: TeamCrudPostInputV1) -> TeamCrudPostOutputV1:
    return TeamCrudPostOutputV1(**{"id": 1})


async def teams__team_id_post_v1(post_input: TeamCrudPostInputV1) -> TeamCrudPostOutputV1:
    return TeamCrudPostOutputV1(**{"id": 1})


async def teams__team_id_delete_v1(post_input: TeamCrudPostInputV1) -> TeamCrudPostOutputV1:
    return TeamCrudPostOutputV1(**{"id": 1})
