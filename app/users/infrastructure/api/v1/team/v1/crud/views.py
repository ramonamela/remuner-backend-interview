from typing import List

from fastapi import HTTPException

from app.users.dependency_injection.application.view_controllers.v1.team.crud.create import (
    CreateTeamViewControllers,
)
from app.users.dependency_injection.application.view_controllers.v1.team.crud.delete import (
    DeleteTeamViewControllers,
)
from app.users.dependency_injection.application.view_controllers.v1.team.crud.get import (
    GetTeamViewControllers,
)
from app.users.dependency_injection.application.view_controllers.v1.team.crud.update import (
    UpdateTeamViewControllers,
)
from app.users.infrastructure.api.v1.team.v1.crud.view_models import (
    TeamCrudIdOutputV1,
    TeamCrudInputV1,
)
from app.users.infrastructure.persistence.exceptions.team_bo import (
    RepeatedTeamNameException,
    TeamNotFoundException,
)


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


async def teams__team_id_post_v1(team_id: int, post_input: TeamCrudInputV1) -> TeamCrudIdOutputV1:
    view_controller = UpdateTeamViewControllers.v1()
    try:
        return await view_controller(team_id=team_id, input_team=post_input)
    except TeamNotFoundException:
        raise HTTPException(status_code=404, detail="Team not found")


async def teams__team_id_delete_v1(team_id: int):
    view_controller = DeleteTeamViewControllers.v1()
    try:
        await view_controller(team_id=team_id)
        return {}
    except TeamNotFoundException:
        raise HTTPException(status_code=404, detail="Team not found")
