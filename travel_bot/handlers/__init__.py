from aiogram import Router

def setup_routers() -> Router:
    from . import place_of_the_day, service_commands, travel_advice, random_tour

    router = Router()
    router.include_router(place_of_the_day.router)
    router.include_router(service_commands.router)
    router.include_router(travel_advice.router)
    router.include_router(random_tour.router)

    return router