from rest_framework import generics

from . import models
from . import serializers


class HeroList(generics.ListCreateAPIView):
    queryset = models.Hero.objects.all()
    serializer_class = serializers.HeroSerializer


class HeroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Hero.objects.all()
    serializer_class = serializers.HeroSerializer
