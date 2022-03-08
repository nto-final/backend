from django.db import models


class Route(models.Model):
    direction = models.CharField(choices=
                                 (('L', 'LEFT'), ('R', 'RIGHT'), ('D', 'DOWN'), ('U', 'UP')), max_length=100)
    distance = models.IntegerField()
    destinationPointId = models.IntegerField()


class Point(models.Model):
    description = models.TextField()
    name = models.TextField()
    marker = models.FileField()
    routes = models.ManyToManyField(Route)
