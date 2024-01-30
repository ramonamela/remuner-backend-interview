from functools import wraps
from typing import Any, Callable, Dict

from fastapi import Response, status
from pydantic import ValidationError


def custom_router_decorator(versions: Dict[Any, Callable]):
    def decorator(func: Callable):
        @wraps(func)
        async def wrapper(*args, response: Response, X_API_Version: str, **kwargs):
            if X_API_Version in versions:
                current_function = versions[X_API_Version]
                for argument in current_function.__annotations__:
                    if not argument == "return":
                        if (
                            argument not in kwargs
                            or not current_function.__annotations__[argument]
                            == kwargs[argument].__class__
                        ):
                            try:
                                kwargs[argument] = current_function.__annotations__[argument](
                                    **kwargs[argument].dict()
                                )
                            except ValidationError:
                                response.status_code = status.HTTP_400_BAD_REQUEST
                                return {"message": "Incorrect body"}
                return await current_function(*args, **kwargs)
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message": "Incorrect header value"}

        return wrapper

    return decorator
