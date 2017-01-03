from channels.binding.websockets import WebsocketBinding

from django.db import models


class Hero(models.Model):
    """
    Represents a Hero.
    """
    name = models.TextField()

    def __str__(self):
        return self.name


class HeroBinding(WebsocketBinding):
    model = Hero
    stream = 'hero'
    fields = ['__all__']

    def group_names(self, instance, action):
        return ['hero-updates']

    def has_permission(self, user, action, pk):
        return True
