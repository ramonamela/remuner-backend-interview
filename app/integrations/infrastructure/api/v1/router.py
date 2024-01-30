from fastapi import APIRouter

from app.integrations.infrastructure.api.v1.integration.router import router as integration_router

router = APIRouter()

router.include_router(integration_router, prefix="", tags=["IntegrationsApp"])
