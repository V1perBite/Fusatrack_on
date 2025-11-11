from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Route, Stop

class RouteSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Route
        geo_field = "path"
        fields = ("id", "name", "color")

class StopSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Stop
        geo_field = "location"
        fields = ("id", "name", "route")