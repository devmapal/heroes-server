from channels.routing import include

from hero_service.routing import hero_service_routing


channel_routing = [
    include(hero_service_routing, path=r"^/heroes-service"),
]
