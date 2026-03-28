import re

sheet = open(0).read()
lines = sheet.splitlines()

number_of_problems = len(re.findall(r"\d+", lines[0]))

symbols = [x for x in lines[-1].split(" ") if x]

# print(symbols)

problems = []
for symbol in symbols:
    if symbol == "+":
        problems.append(0)
    else:
        problems.append(1)

for line in lines:
    numbers = re.findall(r"\d+", line)
    # print(numbers)
    for i, number in enumerate(numbers):
        if symbols[i] == "+":
            problems[i] = problems[i] + int(number)
        else:
            problems[i] = problems[i] * int(number)

count = sum(problems)
print(count)
