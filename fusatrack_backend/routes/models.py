from django.contrib.gis.db import models

class Route(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=7, default="#3388ff")
    path = models.LineStringField()

    def __str__(self):
        return self.name

class Stop(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
    route = models.ForeignKey(Route, related_name="stops", on_delete=models.CASCADE)

    def __str__(self):
        return self.name