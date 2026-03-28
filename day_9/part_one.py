red_tiles = [list(map(int, line.split(","))) for line in open(0).read().splitlines()]
max_rectangle = 0

for i, tile in enumerate(red_tiles):
    current_max = 0
    for second_tile in red_tiles[i:]:
        if current_max < (1 + abs(tile[0] - second_tile[0])) * (
            1 + abs(tile[1] - second_tile[1])
        ):
            current_max = (1 + abs(tile[0] - second_tile[0])) * (
                1 + abs(tile[1] - second_tile[1])
            )

    if current_max > max_rectangle:
        max_rectangle = current_max
print(max_rectangle)
