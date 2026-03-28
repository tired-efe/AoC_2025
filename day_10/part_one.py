from collections import deque

machines = open(0).read().splitlines()

indicators = []
machines_buttons = []


for machine in machines:
    info = machine.split(" ")
    buttons = []
    correct_form = []
    for indicator in info[0].strip("[]"):
        correct_form.append(indicator)
    indicators.append(tuple(correct_form))
    machine_buttons = []
    for buttons in info[1:-1]:
        machine_buttons.append(tuple(map(int, buttons.strip("()").split(","))))
    machines_buttons.append(machine_buttons)
# joltage = []

solution_for_machines = []
for i, machine in enumerate(machines):
    current_machine_options = deque()
    past_options = set()

    for button in machines_buttons[i]:
        lights = ["."] * len(indicators[i])
        for number in button:
            lights[number] = "#"
        current_machine_options.append((1, tuple(lights)))

    while True:
        current_number, current_lights = current_machine_options.popleft()
        if current_lights == indicators[i]:
            solution_for_machines.append(current_number)
            # print(current_number, current_lights)
            break
        if current_lights in past_options:
            continue
        past_options.add(current_lights)

        for button in machines_buttons[i]:
            past_lights = list(current_lights)
            for number in button:
                if past_lights[number] == "#":
                    past_lights[number] = "."
                else:
                    past_lights[number] = "#"
            current_machine_options.append((current_number + 1, tuple(past_lights)))

button_presses = 0
for number in solution_for_machines:
    button_presses += number

print(button_presses)
