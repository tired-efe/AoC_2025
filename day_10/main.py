from collections import deque

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

for i, machine in enumerate(machines):
    print(i)
    current_machine_options = deque()

    joltage = tuple([0] * len(joltage_req[i]))
    current_machine_options.append((0, joltage))
    past_options = {joltage}
    while current_machine_options:
        current_number, current_joltage = current_machine_options.popleft()
        if current_joltage == joltage_req[i]:
            solution_for_machines.append(current_number)
            # print(current_number, current_lights)
            break
        for button in machines_buttons[i]:
            new_joltage = list(current_joltage)
            overflow = False
            for number in button:
                new_joltage[number] += 1
                if new_joltage[number] > joltage_req[i][number]:
                    overflow = True
                    break
            if overflow:
                continue
            if tuple(new_joltage) in past_options:
                continue
            past_options.add(tuple(new_joltage))
            current_machine_options.append((current_number + 1, tuple(new_joltage)))

button_presses = 0
for number in solution_for_machines:
    button_presses += number

print(button_presses)
