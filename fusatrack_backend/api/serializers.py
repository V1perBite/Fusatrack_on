from rest_framework import serializers
from .models import Route, Stop


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ('id', 'name', 'path')  # 'path' debe ser tu campo geométrico


class StopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stop
        fields = ('id', 'name', 'route', 'location')  # 'location' es el campo geométrico
