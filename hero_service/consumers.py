from channels.generic.websockets import WebsocketDemultiplexer

from . import binding

class Demultiplexer(WebsocketDemultiplexer):
    consumers = {
        'hero': binding.HeroBinding.consumer,
    }

    def connection_groups(self):
        return ['hero-updates']
