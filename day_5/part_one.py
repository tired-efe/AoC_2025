a = open(0).read().splitlines()

split_id = a.index("")
fresh_ids = a[:split_id]
igredients = a[(split_id + 1) :]

# print(fresh_ids, igredients)

fresh_igredients = set()
# fresh_ids.sort()
# igredients.sort()
# last_range = 0

for i, igredient in enumerate(igredients):
    for j, fresh_id in enumerate(fresh_ids):
        # for j, fresh_id in enumerate(fresh_ids[last_range:]):

        start, stop = fresh_id.split("-")
        if (int(start) > int(igredient)) or (int(stop) < int(igredient)):
            # last_range += j
            continue
        if (int(stop) - int(start)) >= (int(stop) - int(igredient)):
            # print(start, stop, igredient)
            fresh_igredients.add(igredient)


print(len(fresh_igredients))
