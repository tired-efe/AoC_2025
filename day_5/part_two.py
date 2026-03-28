ranges, _ = open(0).read().split("\n\n")
intervals = sorted(tuple(map(int, line.split("-"))) for line in ranges.splitlines())
# print(intervals)
count = 0
highest = 0

for low, high in intervals:
    if high <= highest:
        continue

    count += high - max(low - 1, highest)
    highest = high

print(count)
