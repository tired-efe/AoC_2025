id_ranges = input().split(",")
# weird_ids = set()
weird_ids_count = 0
for id_range in id_ranges:
    start, finish = id_range.split("-")
    if start[0] == "0":
        continue
    start_n, finish_n = int(start), int(finish)
    for i in range(start_n, finish_n + 1):
        # check the sequence of numbers
        number_as_string = str(i)
        for j in range(2, len(number_as_string) + 1):
            part_n = len(number_as_string) // j
            parts = []
            string_left = number_as_string
            for k in range(j):
                parts.append(string_left[:part_n])
                string_left = string_left[part_n:]
            if string_left != "":
                parts.append(string_left)
            if len(set(parts)) == 1:
                weird_ids_count += i
                # weird_ids.add(i)
                break
                # print(i, parts, k, string_left)
print(weird_ids_count)
# print(weird_ids)
