from channels.generic.websockets import WebsocketDemultiplexer

class Demultiplexer(WebsocketDemultiplexer):
    mapping = {
        'hero': 'binding.hero',
    }

    def connection_groups(self):
        return ['hero-updates']
