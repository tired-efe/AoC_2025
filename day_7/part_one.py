diagram = open(0).read().splitlines()
splitter = "^"
empty = "."

starting_position = diagram[0].index("S")
count = 0
current_position = set()
current_position.add(starting_position)
for line in diagram:
    # print(current_position)
    new_position = set()
    for position in current_position:
        if line[position] == splitter:
            count += 1
            if position - 1 >= 0:
                new_position.add(position - 1)
            if position + 1 < len(line):
                new_position.add(position + 1)
        else:
            new_position.add(position)
    current_position = new_position
print(count)
