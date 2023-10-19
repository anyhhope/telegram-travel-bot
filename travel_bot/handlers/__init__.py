from aiogram import Router

def setup_routers() -> Router:
    from . import place_of_the_day, service_commands

    router = Router()
    router.include_router(place_of_the_day.router)
    router.include_router(service_commands.router)

    return router