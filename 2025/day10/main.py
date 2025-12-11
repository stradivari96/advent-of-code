import typing
import re
from ortools.sat.python import cp_model

class Machine(typing.NamedTuple):
    lights: str
    button_wiring: list[tuple]
    joltage_requirements: list[int]

class Problem(typing.NamedTuple):
    machines: list[Machine]

def main():
    with open("data.txt") as f:
        lines = f.read().splitlines()
    regex = re.compile(r"(\[.*\]) (.*) (\{.*\})")
    machines = []
    for line in lines:
        match = regex.match(line)
        lights_str, button_wiring_str, joltage_requirements_str = match.groups()
        lights = [c == '#' for c in lights_str.strip("[]")]
        button_wiring = [tuple(int(num) for num in t.strip('()').split(',')) for t in button_wiring_str.split(' ')]
        joltage_requirements = list(int(num) for num in joltage_requirements_str.strip('{}').split(','))
        machine = Machine(
            lights=lights,
            button_wiring=button_wiring,
            joltage_requirements=joltage_requirements,
        )
        machines.append(machine)
    problem = Problem(machines=machines)
    print(part_1(problem))
    print(part_2(problem))


def part_1(problem: Problem):
    
    # bfs problem, minimize number of button presses to achieve desired light configuration
    total = 0
    for machine in problem.machines:
        initial_state = tuple(False for _ in machine.lights)
        target_state = tuple(machine.lights)
        queue = [(initial_state, 0)]
        visited = set()
        while queue:
            state, presses = queue.pop(0)
            if state == target_state:
                total += presses
                break
            for button in machine.button_wiring:
                new_state = list(state)
                for idx in button:
                    new_state[idx] = not new_state[idx]
                new_state_tuple = tuple(new_state)
                if new_state_tuple not in visited:
                    visited.add(new_state_tuple)
                    queue.append((new_state_tuple, presses + 1))
    return total


def part_2(problem: Problem):
    total = 0
    for machine in problem.machines:
        model = cp_model.CpModel()
        button_presses = [
            model.NewIntVar(0, cp_model.INT32_MAX, f"button_{i}_presses")
            for i in range(len(machine.button_wiring))
        ]
        for i in range(len(machine.joltage_requirements)):
            buttons = [
                button_presses[j]
                for j, wiring in enumerate(machine.button_wiring)
                if i in wiring
            ]
            model.Add(machine.joltage_requirements[i] == sum(buttons))
        model.Minimize(sum(button_presses))
        solver = cp_model.CpSolver()
        status = solver.Solve(model)
        if status == cp_model.OPTIMAL:
            total += solver.Value(sum(button_presses))
    return total


if __name__ == "__main__":
    main()
