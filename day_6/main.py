import re
import math

sheet = open(0).read()
lines = sheet.splitlines()
columns = list(zip(*lines[:-1])) + [[]]
number_of_problems = len(re.findall(r"\d+", lines[0]))

symbols = (x for x in lines[-1].split(" ") if x)

# print(symbols)

problems = []
count = 0
curent_problem = 0
for column in columns:
    column_s = "".join(column)
    if not column_s.strip():
        symbol = next(symbols)
        if symbol == "+":
            count += sum(problems)
            # print("+", sum(problems))
        else:
            count += math.prod(problems)
            # print("*", math.prod(problems))
        problems.clear()
        continue
    number = int(column_s)
    # print(number)
    problems.append(number)


# count = sum(problems)
print(count)
