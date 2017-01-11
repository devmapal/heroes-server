from channels.binding.websockets import WebsocketBinding

from . import models


class HeroBinding(WebsocketBinding):
    model = models.Hero
    stream = 'hero'
    fields = ['__all__']

    @classmethod
    def group_names(cls, instance):
        return ['hero-updates']

    def has_permission(self, user, action, pk):
        return True
