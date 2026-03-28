# lines_count = 4081
lines_count = 4081
rotations = [input() for _ in range(lines_count)]
current_dial = 50
count_zero = 0

for rotation in rotations:
    if rotation[0] == "L":
        way = -1
    else:
        way = 1
    i = int(rotation[1:])
    if i >= 100:
        i = i % 100
    if current_dial + way * i > 99:
        left = current_dial + way * i - 99
        current_dial = left - 1
    elif current_dial + way * i < 0:
        left = i - current_dial
        current_dial = 99 - left + 1
    else:
        current_dial += way * i
    if current_dial == 0:
        count_zero += 1
print(count_zero)
