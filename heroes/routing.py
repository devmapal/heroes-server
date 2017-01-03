from channels.routing import include, route, route_class

from hero_service.consumers import Demultiplexer
from hero_service.models import HeroBinding


channel_routing = [
    route_class(Demultiplexer, path="^/api/heroes"),
    route('binding.hero', HeroBinding.consumer),
]
