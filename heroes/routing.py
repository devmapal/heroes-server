from channels.routing import include, route, route_class

from hero_service.consumers import Demultiplexer
from hero_service.models import HeroBinding


channel_routing = [
    route_class(Demultiplexer, path="^/api/ws"),
    route('binding.hero', HeroBinding.consumer),
]
