banks = open(0).read().splitlines()

total_joltage = 0

for bank in banks:
    batteries = list(bank)
    max_joltage = 0
    last_index = -1
    digits = []
    indexes_left = 12
    computing_index = 0

    while indexes_left > 0:
        a = len(batteries) - indexes_left + 1
        batteries_left = batteries[(last_index + 1) : a]
        current_digit = max(batteries_left)
        current_index = batteries_left.index(current_digit)
        last_index += current_index + 1
        digits.append(current_digit)
        indexes_left -= 1
        computing_index += 1
    max_joltage = "".join(digits)
    total_joltage += int(max_joltage)
print(total_joltage)
