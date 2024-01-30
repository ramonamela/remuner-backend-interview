from typing import Any, Dict, Callable
from functools import wraps
from fastapi import Response, status

def custom_router_decorator(versions: Dict[Any, Callable]):
    def decorator(func: Callable):
        @wraps(func)
        async def wrapper(*args, response: Response, X_API_Version: str, **kwargs):
            # Your custom logic here before handling the route
            if X_API_Version in versions:
                return await versions[X_API_Version](*args, **kwargs)
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message": "Incorrect header value"}
        return wrapper
    return decorator
