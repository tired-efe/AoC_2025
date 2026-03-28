id_ranges = input().split(",")
weird_ids = []
weird_ids_count = 0
for id_range in id_ranges:
    start, finish = id_range.split("-")
    if start[0] == "0":
        continue
    start_n, finish_n = int(start), int(finish)
    for i in range(start_n, finish_n + 1):
        # check the sequence of numbers
        number_as_string = str(i)
        first_half = number_as_string[: len(number_as_string) // 2]
        second_half = number_as_string[len(number_as_string) // 2 :]
        if first_half == second_half:
            weird_ids_count += i

print(weird_ids_count)
