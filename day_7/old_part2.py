from collections import deque

diagram = open(0).read().splitlines()
splitter = "^"
empty = "."

starting_position = diagram[0].index("S")
count = 0

positions = deque()
positions.append((1, starting_position))
# (line,collum)


while True:
    current_line, current_collum = positions.pop()
    if current_line == len(diagram) - 1:
        count += 1
    else:
        for i, line in enumerate(diagram[current_line:]):
            if i + current_line == len(diagram) - 1:
                count += 1
                break
            if line[current_collum] == splitter:
                if current_collum - 1 >= 0:
                    positions.append((current_line + i, current_collum - 1))
                if current_collum + 1 < len(line):
                    positions.append((current_line + i, current_collum + 1))
                break
    if not positions:
        break
    # print(positions)
    # print(count)
print(count)
