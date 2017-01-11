from channels.routing import route_class

from hero_service.consumers import Demultiplexer


channel_routing = [
    route_class(Demultiplexer, path="^/api/ws"),
]
