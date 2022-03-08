from rest_framework.serializers import ModelSerializer, Serializer, PrimaryKeyRelatedField
from navigation.models import Route, Point
from .utils import dfs

class PointSerializer(ModelSerializer):
    class Meta:
        model = Point
        fields = "__all__"


class RouteSerializer(ModelSerializer):
    class Meta:
        model = Route
        fields = "__all__"


class GetShortestPathSerializer(Serializer):
    starting_point = PrimaryKeyRelatedField(queryset=Point.objects.all(), write_only=True)
    ending_point = PrimaryKeyRelatedField(queryset=Point.objects.all(), write_only=True)
    routes = PrimaryKeyRelatedField(read_only=True, many=True)

    def create(self, validated_data):
        return {"routes": dfs(validated_data['starting_point'], validated_data['ending_point'], [], [])}
