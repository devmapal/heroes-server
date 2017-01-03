from django.db import models

class Hero(models.Model):
    """
    Represents a Hero.
    """
    name = models.TextField()

    def __str__(self):
        return self.name
