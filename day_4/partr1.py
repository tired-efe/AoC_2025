paper_map = open(0).read().splitlines()
count = 0

adjacnet_position = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, -1],
    [0, 1],
    [1, -1],
    [1, 0],
    [1, 1],
]
number_of_rows = len(paper_map)
for i, row in enumerate(paper_map):
    for j, element in enumerate(row):
        if element == "@":
            adjacnet = 0
            for position in adjacnet_position:
                check_row = i + position[0]
                check_collum = j + position[1]
                if (
                    check_collum < number_of_rows
                    and check_row >= 0
                    and check_row < len(row)
                    and check_collum >= 0
                ):
                    if paper_map[check_row][check_collum] == "@":
                        adjacnet += 1
            if adjacnet < 4:
                count += 1

print(count)
