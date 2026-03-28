a = open(0).read().splitlines()

split_id = a.index("")
fresh_ids = a[:split_id]
count = 0
conflicts_ranges = []
conflicst_i = []

for i, fresh_id_range in enumerate(fresh_ids):
    start, stop = fresh_id_range.split("-")
    start, stop = int(start), int(stop)
    # print("starting new")
    # print("new", start, stop)
    for other_id in fresh_ids[:i]:
        other_start, other_stop = other_id.split("-")
        other_start, other_stop = int(other_start), int(other_stop)
        # print("other start", other_start, "other stop", other_stop)
        if start > other_stop or stop < other_start:
            continue
        if (stop >= other_stop) and (start >= other_start):
            start = other_stop + 1

        if (stop <= other_stop) and (start <= other_start):
            stop = other_start - 1

        if (stop <= other_stop) and (start >= other_start):
            start = 1
            stop = 0
            break
        if (stop >= other_stop) and (start <= other_start):
            conflicts_ranges.append(str(start) + "-" + str(other_start))
            conflicts_ranges.append(str(stop) + "-" + str(stop))
            conflicst_i.append(i)
            conflicst_i.append(i)
        # check if interval
        # modify start/ stop
    # print("ends at", start)
    count += stop - start + 1

while True:
    current_conflicts_i = conflicst_i.copy()
    current_conflicts_ranges = conflicts_ranges.copy()

    conflicts_ranges = []
    conflicst_i = []
    for i, fresh_id_range in enumerate(current_conflicts_ranges):
        start, stop = fresh_id_range.split("-")
        start, stop = int(start), int(stop)
        # print("starting new")
        # print("new", start, stop)

        for j, other_id in enumerate(fresh_ids):
            if j == current_conflicts_i[i]:
                continue
            other_start, other_stop = other_id.split("-")
            other_start, other_stop = int(other_start), int(other_stop)
            # print("other start", other_start, "other stop", other_stop)
            if start > other_stop or stop < other_start:
                continue
            if (stop >= other_stop) and (start >= other_start):
                start = other_stop + 1

            if (stop <= other_stop) and (start <= other_start):
                stop = other_start - 1

            if (stop <= other_stop) and (start >= other_start):
                start = 1
                stop = 0
                break
            if (stop >= other_stop) and (start <= other_start):
                conflicts_ranges.append(str(start) + "-" + str(other_start))
                conflicts_ranges.append(str(stop) + "-" + str(stop))
                conflicst_i.append(i)

        count += stop - start + 1
    if len(conflicst_i) == 0:
        break
print(count)
