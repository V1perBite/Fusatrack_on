from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Route, Stop
from .serializers import RouteSerializer, StopSerializer


# Vista de prueba
def test(request):
    return JsonResponse({"message": "Fusatrack backend funcionando correctamente"})


# ViewSets para DRF (si quieres usar routers)
class RouteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

class StopViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Stop.objects.all()
    serializer_class = StopSerializer


# APIViews para endpoints directos
class RouteListAPIView(APIView):
    """
    Devuelve todas las rutas en formato GeoJSON.
    """
    def get(self, request):
        routes = Route.objects.all()
        serializer = RouteSerializer(routes, many=True)
        return Response(serializer.data)


class StopListAPIView(APIView):
    """
    Devuelve todas las paradas en formato GeoJSON.
    """
    def get(self, request):
        stops = Stop.objects.all()
        serializer = StopSerializer(stops, many=True)
        return Response(serializer.data)
