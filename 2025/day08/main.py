import itertools
import typing

class Problem(typing.NamedTuple):
    boxes: list[tuple[int, int, int]]

def main():
    with open("data.txt") as f:
        lines = f.read().splitlines()
    problem = Problem(boxes=[
        tuple(int(x) for x in line.split(','))
        for line in lines
    ])
    print(part_1(problem))
    print(part_2(problem))


class UnionFind:
    def __init__(self):
        self.f = {}

    def findParent(self, x):
        y = self.f.get(x, x)
        if x != y:
            y = self.f[x] = self.findParent(y)
        return y

    def union(self, x, y):
        self.f[self.findParent(x)] = self.findParent(y)



def part_1(problem: Problem):
    connections = 1000
    dist_map = {
        (i, j): (problem.boxes[i][0] - problem.boxes[j][0])**2 + (problem.boxes[i][1] - problem.boxes[j][1])**2 + (problem.boxes[i][2] - problem.boxes[j][2])**2
        for i, j in itertools.combinations(range(len(problem.boxes)), 2)
    }
    sorted_dist = sorted(dist_map.items(), key=lambda x: x[1])
    uf = UnionFind()
    for (i, j), _ in sorted_dist[:connections]:
        uf.union(i, j)
    comp_sizes = {}
    for i in range(len(problem.boxes)):
        p = uf.findParent(i)
        comp_sizes[p] = comp_sizes.get(p, 0) + 1
    three_largest = sorted(comp_sizes.values(), reverse=True)[:3]
    result = 1
    for size in three_largest:
        result *= size
    return result


def part_2(problem: Problem):
    dist_map = {
        (i, j): (problem.boxes[i][0] - problem.boxes[j][0])**2 + (problem.boxes[i][1] - problem.boxes[j][1])**2 + (problem.boxes[i][2] - problem.boxes[j][2])**2
        for i, j in itertools.combinations(range(len(problem.boxes)), 2)
    }
    sorted_dist = sorted(dist_map.items(), key=lambda x: x[1])
    uf = UnionFind()
    for (i, j), _ in sorted_dist:
        uf.union(i, j)
        if all(uf.findParent(0) == uf.findParent(k) for k in range(len(problem.boxes))):
            return problem.boxes[i][0] * problem.boxes[j][0]


if __name__ == "__main__":
    main()
