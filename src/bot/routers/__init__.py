from aiogram import Router

from bot.routers.admin_router import router as admin_router
from bot.routers.commands_router import router as command_router
from bot.routers.common_router import router as common_router
from bot.routers.volunteer_router import router as volunteer_router

router = Router()
router.include_routers(command_router, admin_router, volunteer_router)
router.include_router(common_router)
