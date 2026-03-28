import functools

servers = open(0).read().splitlines()
info = dict()
for server in servers:
    name, destionations = server.split(":")
    outs = []
    for one in destionations.split(" "):
        if one == "":
            continue
        outs.append(one)
    info[name.strip()] = outs

# print(info)

start = "svr"
end = "out"

control_1 = "fft"
control_2 = "dac"


@functools.cache
def count_ways(start_name, stop_name):
    if start_name == stop_name:
        return 1

    count = 0
    if start_name == end:
        return 0
    for path in info[start_name]:
        count += count_ways(path, stop_name)
    return count


print(
    (count_ways(start, control_1))
    * (count_ways(control_1, control_2))
    * (count_ways(control_2, end))
    + (count_ways(start, control_2))
    * (count_ways(control_2, control_1))
    * (count_ways(control_1, end))
)
