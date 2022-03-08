from django.urls import path
from .views import GetPoint, GetPoints, GetRoute, GetRoutes, GetShortestPath


urlpatterns = [
    path("points", GetPoints.as_view()),
    path("point/<pk>", GetPoint.as_view()),
    path("routes", GetRoutes.as_view()),
    path("route/<pk>", GetRoute.as_view()),
    path("get-shortest-path", GetShortestPath.as_view())
]