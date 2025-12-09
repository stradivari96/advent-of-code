import itertools
import typing
import heapq

class Problem(typing.NamedTuple):
    tiles: list[tuple[int, int]]

def main():
    with open("data.txt") as f:
        lines = f.read().splitlines()
    problem = Problem(tiles=[
        tuple(int(x) for x in line.split(','))
        for line in lines
    ])
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
            if x_start == x_end:
                # this is | vertical edge, x is constant
                if x_start <= x1:
                    continue  # to the left of rectangle
                if x_start >= x2:
                    continue  # to the right of rectangle
                if y_end <= y1:
                    continue  # below rectangle
                if y_start >= y2:
                    continue  # above rectangle
                # intersects
                return False
            else:
                # this is - horizontal edge, y is constant
                if y_start >= y2:
                    continue  # above rectangle
                if y_start <= y1:
                    continue  # below rectangle
                if x_end <= x1:
                    continue  # left of rectangle
                if x_start >= x2:
                    continue  # right of rectangle
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
