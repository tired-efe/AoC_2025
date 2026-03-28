from itertools import pairwise

red_tiles = [list(map(int, line.split(","))) for line in open(0).read().splitlines()]

green_boundary = list(pairwise(red_tiles + [red_tiles[0]]))

print(green_boundary)
max_rectangle = 0

for i, tile in enumerate(red_tiles):
    # tile = [x1,y1]
    current_max = 0
    for j, second_tile in enumerate(red_tiles[i+1:]):
        x1, y1 = tile
        x2, y2 = second_tile
        # second_tile = [x2,y2]
        area = (1 + abs(x1 - x2)) * (1 + abs(y1 - y2))

        if current_max < area:
            lower_x = min(x1,x2)
            lower_y = min(y1,y2)
            higher_x = max(x1,x2)
            higher_y = max(y1,y2)
            only_green = True
            
            for x in range(lower_x+1,higher_x):
                
            # print(tile, second_tile, only_green)
            # print(area, max_rectangle)
            if only_green:
                current_max = area

    if current_max > max_rectangle:
        max_rectangle = current_max
print(max_rectangle)
