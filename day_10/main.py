from collections import deque
import numpy as np
from scipy.optimize import linprog


def apply(state: tuple[int, ...], button: tuple[int, ...]):
    new_state = list(state)
    for index in button:
        new_state[index] += 1
    return new_state


machines = open(0).read().splitlines()

machines_buttons = []
joltage_req = []

for machine in machines:
    info = machine.split()

    machine_buttons = []
    for button in info[1:-1]:
        machine_buttons.append(tuple(map(int, button.strip("()").split(","))))
    machines_buttons.append(machine_buttons)

    joltage_req.append(tuple(map(int, info[-1].strip("{}").split(","))))
# joltage = []

# print(joltage_req)
solution_for_machines = []

total = 0
# print(f"{machines_buttons = }")
# print(f"{joltage_req = }")

for target, buttons in zip(joltage_req, machines_buttons):
    vectors = [apply(tuple(0 for _ in target), button) for button in buttons]

    a_eq = np.stack(vectors, axis=1, dtype=np.int64)
    b_eq = np.array(target, dtype=np.int64)
    c = np.ones(len(vectors), dtype=np.int64)
    result = linprog(c, A_eq=a_eq, b_eq=b_eq, integrality=1)

    if result.success:
        total += round(result.fun)
    else:
        raise ValueError("No solution")
print(total)
