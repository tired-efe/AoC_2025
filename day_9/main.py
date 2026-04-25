from itertools import combinations, pairwise
from math import dist

red_tiles = [tuple(map(int, line.split(","))) for line in open(0).read().splitlines()]

rectengles = combinations(red_tiles, 2)

areas_rectengles: list[tuple[int, tuple[tuple[int, int], tuple[int, int]]]] = []
for duo in rectengles:
    tile, second_tile = duo
    x1, y1 = tile
    x2, y2 = second_tile
    area = (1 + abs(x1 - x2)) * (1 + abs(y1 - y2))
    areas_rectengles.append((area, duo))

areas_rectengles.sort(reverse=True)
# print(areas_rectengles[:100])

edges = sorted(
    ((dist(*edge), edge) for edge in pairwise(red_tiles + [red_tiles[0]])), reverse=True
)

for area, duo in areas_rectengles:
    tile, second_tile = duo
    x1, y1 = tile
    x2, y2 = second_tile

    for _, edge in edges:
        e1, e2 = edge
        e1x, e1y = e1
        e2x, e2y = e2

        ex_min = min(e1x, e2x)
        ex_max = max(e1x, e2x)
        ey_min = min(e1y, e2y)
        ey_max = max(e1y, e2y)

        x_min = min(x1, x2)
        x_max = max(x1, x2)
        y_min = min(y1, y2)
        y_max = max(y1, y2)

        x_inside = ex_min > x_min and ex_max < x_max
        y_inside = ey_min > y_min and ey_min < y_max

        if x_inside and y_inside:
            break
        if x_inside and (ey_min < y_min and ey_max > y_min):
            break
        if x_inside and (ey_min < y_max and ey_max > y_max):
            break
        if y_inside and (ex_min < x_min and ex_max > x_min):
            break
        if y_inside and (ex_min < x_max and ex_max > x_max):
            break
    else:
        print(area)
        break
