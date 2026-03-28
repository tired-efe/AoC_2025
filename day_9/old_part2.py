red_tiles = [list(map(int, line.split(","))) for line in open(0).read().splitlines()]

green_tiles = set()
green_boundary = set()
# Boundary
for i, tile in enumerate(red_tiles):
    if i == len(red_tiles) - 1:
        second_tile = red_tiles[0]
    else:
        second_tile = red_tiles[i + 1]
    if second_tile[0] == tile[0]:
        index = 1
    else:
        index = 0
    for j in range(
        min(tile[index], second_tile[index]) + 1, max(tile[index], second_tile[index])
    ):
        if index == 1:
            green_boundary.add((tile[0], j))
        else:
            green_boundary.add((j, tile[1]))

# doplnit ty z toho loopu

green_loop = set()

for i, tile in enumerate(green_boundary):
    for j, second_tile in enumerate(green_boundary):
        if second_tile[0] == tile[0]:
            index = 1
        elif second_tile[1] == tile[1]:
            index = 0
        else:
            continue
        for k in range(
            min(tile[index], second_tile[index]) + 1,
            max(tile[index], second_tile[index]),
        ):
            if index == 1:
                green_loop.add((tile[0], k))
            else:
                green_loop.add((k, tile[1]))

green_tiles = green_boundary | green_loop


max_rectangle = 0

print("red tiles", red_tiles)
print("green tiles", green_tiles)

for i, tile in enumerate(red_tiles):
    # tile = [x1,y1]
    current_max = 0
    for j, second_tile in enumerate(red_tiles[i:]):
        # second_tile = [x2,y2]
        area = (1 + abs(tile[0] - second_tile[0])) * (1 + abs(tile[1] - second_tile[1]))

        if current_max < area:
            x1, y1 = tile
            x2, y2 = second_tile
            only_green = True
            for x in range(min(x1, x2) + 1, max(x1, x2)):
                for y in range(min(y1, y2) + 1, max(y1, y2)):
                    if (x, y) not in green_tiles:
                        only_green = False
            # print(tile, second_tile, only_green)
            # print(area, max_rectangle)
            if only_green:
                current_max = area

    if current_max > max_rectangle:
        max_rectangle = current_max
print(max_rectangle)
