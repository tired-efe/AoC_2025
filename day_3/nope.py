banks = open(0).read().splitlines()

total_joltage = 0

for bank in banks:
    batteries = [bank[i] for i in range(len(bank))]
    max_joltage = 0
    a = len(batteries) - 11
    batteries2 = batteries[:a]
    fist_digit = max(batteries2)
    first_index = batteries.index(fist_digit)
    indexes = 12 * [None]
    indexes[0] = first_index
    digits = 12 * [None]
    digits[0] = fist_digit
    # print(fist_digit)

    indexes_left = 11
    computing_index = 1
    while indexes_left > 0:
        a = len(batteries) - indexes_left + 1
        batteries_left = batteries[(indexes[computing_index - 1] + 1) : a]
        if batteries_left == []:
            batteries_left = batteries[a]
        if indexes_left == 1:
            batteries_left = batteries[(indexes[computing_index - 1] + 1) :]
        # print(batteries_left, indexes, digits)
        # print(batteries_left, digits)
        current_digit = max(batteries_left)
        indexes[computing_index] = (
            indexes[computing_index - 1] + batteries_left.index(current_digit) + 1
        )
        digits[computing_index] = current_digit
        indexes_left -= 1
        computing_index += 1
    max_joltage = "".join(str(x) for x in digits)
    # print(max_joltage)
    total_joltage += int(max_joltage)
    # print(max_joltage, first_index, second_index)
print(total_joltage)
