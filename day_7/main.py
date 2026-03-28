diagram = open(0).read().splitlines()
splitter = "^"

starting_position = diagram[0].index("S")

timelines_for_splitters = dict()  # (line,columm) : int(count)
all_lines = len(diagram)

for i, line in enumerate(reversed(diagram)):
    for collum_index, character in enumerate(line):
        if character == splitter:
            line_index = all_lines - 1 - i
            collum_plus = True
            collum_minus = True
            plus_count = 1
            minus_count = 1

            for checked_lines in range(i):
                if collum_minus and (
                    (line_index + 1 + checked_lines, collum_index - 1)
                    in timelines_for_splitters
                ):
                    minus_count = timelines_for_splitters[
                        (line_index + 1 + checked_lines, collum_index - 1)
                    ]
                    collum_minus = False

                if collum_plus and (
                    (line_index + 1 + checked_lines, collum_index + 1)
                    in timelines_for_splitters
                ):
                    plus_count = timelines_for_splitters[
                        (line_index + 1 + checked_lines, collum_index + 1)
                    ]
                    collum_plus = False
            count = plus_count + minus_count
            timelines_for_splitters[(line_index, collum_index)] = count


count_plus = 1
minus_count = 1

splitter_found = False

line_index = 1
while True:
    if splitter_found:
        break
    if diagram[line_index][starting_position] == splitter:
        count = timelines_for_splitters[(line_index, starting_position)]
        splitter_found = True
    line_index += 1

print(count)
