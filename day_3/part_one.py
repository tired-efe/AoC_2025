banks = open(0).read().splitlines()

total_joltage = 0

for bank in banks:
    batteries = [bank[i] for i in range(len(bank))]
    max_joltage = 0
    batteries2 = batteries.copy()
    batteries2.pop()
    fist_digit = max(batteries2)
    first_index = batteries.index(fist_digit)
    second_index = None
    for i, baterry in enumerate(batteries):
        if i <= first_index:
            continue
        if int(fist_digit) * 10 + int(baterry) > max_joltage:
            max_joltage = int(fist_digit) * 10 + int(baterry)
            second_index = i
    total_joltage += max_joltage
    # print(max_joltage, first_index, second_index)
print(total_joltage)
