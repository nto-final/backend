from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from .serializers import PointSerializer, RouteSerializer, GetShortestPathSerializer
from navigation.models import Point, Route


class GetPoints(ListAPIView):
    serializer_class = PointSerializer
    queryset = Point.objects.all()


class GetRoutes(ListAPIView):
    serializer_class = RouteSerializer
    queryset = Route.objects.all()


class GetPoint(RetrieveAPIView):
    serializer_class = PointSerializer
    queryset = Point.objects.all()


class GetRoute(RetrieveAPIView):
    serializer_class = RouteSerializer
    queryset = Route.objects.all()


class GetShortestPath(CreateAPIView):
    serializer_class = GetShortestPathSerializer
