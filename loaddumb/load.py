from django.core.files import File
from navigation.models import Point, Route


def load_points():
    vertex_list = [
        [[2, "L"], [3, "R"]],
        [[1, "D"], [5, "L"]],
        [[4, "U"], [1, "R"]],
        [[3, "D"], [8, "L"]],
        [[6, "R"], [2, "D"]],
        [[5, "D"], [7, "R"]],
        [[6, "L"], [8, "R"]],
        [[4, "D"], [7, "U"]]
    ]
    Point.objects.all().delete()
    Route.objects.all().delete()
    for i in range(8):
        f = open('loaddumb/files/{}.zpt'.format(i+1), 'rb')
        file = File(f)
        print(file)
        point = Point.objects.create(name="Объект {}".format(i+1), description="descr", marker=file)
        for j in vertex_list[i]:
            point.routes.add(Route.objects.create(direction=j[1],
                                                  distance=1,
                                                  destinationPointId=j[0]-1 + list(
                                                      sorted(map(lambda x: x.id, Point.objects.all())))[0]))
