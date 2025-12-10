import itertools
import typing
import re

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
        lights = lights_str.strip("[]")
        button_wiring = [tuple(int(num) for num in t.strip('()').split(',')) for t in button_wiring_str.split(' ')]
        joltage_requirements = [list(int(num) for num in joltage_requirements_str.strip('{}').split(','))]
        machine = Machine(
            lights=lights,
            button_wiring=button_wiring,
            joltage_requirements=joltage_requirements,
        )
        machines.append(machine)
    problem = Problem(machines=machines)
    print(problem)
    part1_result, heap = part_1(problem)
    print(part1_result)
    print(part_2(problem, heap))


def part_1(problem: Problem):
    largest_area = 0
    heap = []
    for (x1, y1), (x2, y2) in itertools.combinations(problem.tiles, 2):
        area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        if area > largest_area:
            largest_area = area
        heapq.heappush(heap, (-area, (x1, y1), (x2, y2)))
    return largest_area, heap


def part_2(problem: Problem, heap):
    poly_loop = problem.tiles + [problem.tiles[0]]
    edges = list(zip(poly_loop, poly_loop[1:]))

    def is_valid_rectangle(x1, y1, x2, y2):
        x1, x2 = sorted((x1, x2))
        y1, y2 = sorted((y1, y2))

        for (u_x, u_y), (v_x, v_y) in edges:
            x_start, x_end = sorted((u_x, v_x))
            y_start, y_end = sorted((u_y, v_y))
            # all edges are either vertical or horizontal!!
            if x_end <= x1 or x_start >= x2:
                continue  # to the left or to the right of the rectangle
            if y_end <= y1 or y_start >= y2:
                continue  # above or below the rectangle
            # intersects
            return False
        return True

    # Iterate through rectangles from largest to smallest
    while heap:
        area, (x1, y1), (x2, y2) = heapq.heappop(heap)
        
        if is_valid_rectangle(x1, y1, x2, y2):
            return -area



if __name__ == "__main__":
    main()
