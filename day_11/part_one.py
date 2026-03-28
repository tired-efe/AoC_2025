from collections import deque

servers = open(0).read().splitlines()
names = []
outputs = []
for server in servers:
    name, destionations = server.split(":")
    names.append(name.strip())
    outs = []
    for one in destionations.split(" "):
        if one == "":
            continue
        outs.append(one)
    outputs.append(outs)

count = 0
positions = deque()

positions.append(names.index("you"))
end = "out"
while True:
    current_position = positions.pop()
    for position in outputs[current_position]:
        if position == end:
            count += 1
        else:
            positions.append(names.index(position))
    if not positions:
        break
print(count)
