coordinates = [list(map(int, line.split(","))) for line in open(0).read().splitlines()]


def distance(first, second):
    return (
        (first[0] - second[0]) ** 2
        + (first[1] - second[1]) ** 2
        + (first[2] - second[2]) ** 2
    ) ** (1 / 2)


circuits: list[set[int]] = []  # [[index1, index2, ...],[index1, ...]]
connected = set()  #
distances = []

# compute distances, in an array as [int distance, index1, index2]
for index1 in range(len(coordinates)):
    for index2 in range(index1 + 1, len(coordinates)):
        distances.append(
            [distance(coordinates[index1], coordinates[index2]), index1, index2]
        )
# compute distances, in an array as [int distance, index1, index2]
distances.sort()  # sort it

for _, index1, index2 in distances:
    circuit_of_index1, circuit_of_index2 = None, None

    if index1 in connected:
        for i, circuit in enumerate(circuits):
            if index1 in circuit:
                circuit_of_index1 = i
    if index2 in connected:
        for i, circuit in enumerate(circuits):
            if index2 in circuit:
                circuit_of_index2 = i

    if circuit_of_index1 is not None and circuit_of_index2 is not None:
        if circuit_of_index1 == circuit_of_index2:
            continue

        else:
            part1 = circuits[circuit_of_index1]
            part2 = circuits[circuit_of_index2]
            circuits.append(part1 | part2)
            circuits[circuit_of_index1] = []
            circuits[circuit_of_index2] = []
            continue

    if circuit_of_index1 is not None:
        circuits[circuit_of_index1].add(index2)
        connected.add(index2)
        continue

    if circuit_of_index2 is not None:
        circuits[circuit_of_index2].add(index1)
        connected.add(index1)
        continue
    connected.add(index1)
    connected.add(index2)
    circuits.append({index1, index2})

lengths = [len(circuit) for circuit in circuits]
lengths.sort(reverse=True)
print(lengths)
length = lengths[0] * lengths[1] * lengths[2]
print(length)
# found the new shortest that is not already connected
# check if it is already part of a cirtcuit (for both)
