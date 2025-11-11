from django.contrib.gis.db import models

class Route(models.Model):
    name = models.CharField(max_length=100)
    path = models.LineStringField()  # Línea que representa la ruta
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Stop(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()  # Punto geográfico
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='stops')

    def __str__(self):
        return self.name
