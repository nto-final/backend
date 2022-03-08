from navigation.models import Point, Route


def dfs(starting_point: Point, ending_point: Point, current_paths: list, visited: list) -> [Route]:
    v = starting_point
    for i in v.routes.all():
        if i.destinationPointId in visited: continue
        if i.destinationPointId == ending_point.id:
            return current_paths + [i]
        else:
            visited.append(i.destinationPointId)
            return dfs(Point.objects.get(id=i.destinationPointId), ending_point, current_paths + [i], visited)
