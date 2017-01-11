from channels.generic.websockets import WebsocketDemultiplexer

from . import binding

class Demultiplexer(WebsocketDemultiplexer):
    mapping = {
        'hero': binding.HeroBinding,
    }

    def connection_groups(self):
        return ['hero-updates']
