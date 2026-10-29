from aiogram import Router

from .start import router as start_router
from .form import router as form_router


def setup_routers() -> Router:
    root = Router()
    root.include_router(start_router)
    root.include_router(form_router)
    return root
