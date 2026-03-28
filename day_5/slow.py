a = open(0).read().splitlines()

split_id = a.index("")
fresh_ids = a[:split_id]
igredients = a[(split_id + 1) :]

fresh_ids_set = set()

count = 0
for fresh_id in fresh_ids:
    start, stop = fresh_id.split("-")
    # fresh_ids_set.add(i for i in range(int(start), int(stop) + 1))
    for i in range(int(start), int(stop) + 1):
        fresh_ids_set.add(i)
# print(fresh_ids_set)

for igredient in igredients:
    if int(igredient) in fresh_ids_set:
        count += 1
print(count)
