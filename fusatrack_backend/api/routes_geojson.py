from rest_framework.decorators import api_view
from rest_framework.response import Response
from routes.models import Route  # 👈 importa tu modelo Route

@api_view(['GET'])
def route_list(request):
    routes = Route.objects.all()
    data = []

    for route in routes:
        # El campo "path" es un objeto LineString de GeoDjango
        coords = list(route.path.coords)  # [(lng, lat), (lng, lat), ...]

        # Convertimos a lista de diccionarios {lat, lng}
        points = [{"lat": lat, "lng": lng} for (lng, lat) in coords]

        data.append({
            "id": route.id,
            "name": route.name,
            "points": points,
        })

    return Response(data)
