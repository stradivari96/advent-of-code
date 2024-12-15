
def main():
    with open("data.txt") as f:
        matrix = f.read().splitlines()
        matrix = [list(row) for row in matrix]
    original_matrix = [row.copy() for row in matrix]
    print(part_1(original_matrix))
    print(part_2(original_matrix))


def move(x, y, visited, matrix, direction):
    rotate = {
        (0, -1): (-1, 0),
        (1, 0): (0, -1),
        (0, 1): (1, 0),
        (-1, 0): (0, 1),
    }
    while True:
        if x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0]):
            return None
        if matrix[x][y] != "#":
            visited.add((x, y))
        if matrix[x][y] == "#":
            return x-direction[0], y-direction[1], rotate[direction]
        x += direction[0]
        y += direction[1]


def part_1(matrix: list[str]):
    start_pos = next((i, j) for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j] in "^v<>")
    visited = set()
    x, y = start_pos
    direction = get_direction(x, y, matrix)
    while new := move(x, y, visited, matrix, direction):
        (x, y, direction) = new
    return len(visited)


def part_2(matrix: list[tuple[int]]):
    original_matrix = [row.copy() for row in matrix]
    start_pos = next((i, j) for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j] in "^v<>")
    visited = set()
    x, y = start_pos
    direction = get_direction(x, y, matrix)
    while new := move(x, y, visited, matrix, direction):
        (x, y, direction) = new

    result = 0
    for (x, y) in visited:
        if (x, y) == start_pos:
            continue
        matrix = [row.copy() for row in original_matrix]
        matrix[x][y] = "#"
        if check_loop(start_pos[0], start_pos[1], matrix):
            result += 1
    return result


def check_loop(x, y, matrix):
    visited = set()
    seen_counter = {}
    direction = get_direction(x, y, matrix)
    while new := move(x, y, visited, matrix, direction):
        (x, y, direction) = new
        seen_counter[(x, y)] = seen_counter.get((x, y), 0) + 1
        if seen_counter[(x, y)] == 5:
            return True
    return False


def get_direction(x, y, matrix):
    if matrix[x][y] == "^":
        direction = (-1, 0)
    elif matrix[x][y] == "v":
        direction = (1, 0)
    elif matrix[x][y] == "<":
        direction = (0, -1)
    elif matrix[x][y] == ">":
        direction = (0, 1)
    return direction
 
if __name__ == "__main__":
    main()
