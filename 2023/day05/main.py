from concurrent.futures import ProcessPoolExecutor
from typing import NamedTuple
from functools import partial


class Problem(NamedTuple):
    seeds: list[int]
    seed_to_soil: dict[tuple[int], int]
    soil_to_fertilizer: dict[tuple[int], int]
    fertilizer_to_water: dict[tuple[int], int]
    water_to_light: dict[tuple[int], int]
    light_to_temperature: dict[tuple[int], int]
    temperature_to_humidity: dict[tuple[int], int]
    humidity_to_location: dict[tuple[int], int]


def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    seeds = [int(s) for s in lines.pop(0).split("seeds: ")[1].split(" ")]
    maps = _parse_maps(lines)
    problem = Problem(seeds, *maps)
    print(part_1(problem))
    print(part_2(problem))


def _parse_maps(lines: list[str]):
    lines = lines[::-1]
    current_map = None
    result = []
    while lines:
        line = lines.pop()
        if "map" in line:
            current_map = {}
            continue
        while line != "":
            dst, start, length = [int(n) for n in line.split(" ")]
            current_map[start, start+length-1] = dst
            if not lines:
                break
            line = lines.pop()
        if current_map:
            result.append(current_map)
    return result


def part_1(problem: Problem):
    locations = []
    for seed in problem.seeds:
        n = seed
        for mapping in problem[1:]:
            n = map_next(n, mapping)
        locations.append(n)
    return min(locations)


def map_next(n, mapping):
    for (start, end), v in mapping.items():
        if start > n or end < n:
            continue
        return v+(n-start)
    return n


def part_2(problem: Problem):
    # probably could do some binary search / detect monotonic etc
    seed_ranges = [(problem, r) for r in get_seed_ranges(problem.seeds)]
    process_seed_range_1000 = partial(process_seed_range, step=1000)
    with ProcessPoolExecutor() as executor:
        values = executor.map(process_seed_range_1000, seed_ranges)
    values = list(values)

    good_range = values.index(min(values))
    process_seed_range_1 = partial(process_seed_range, step=1)
    seed_ranges = [(problem, r) for r in create_chunks(seed_ranges[good_range][1], 8)]
    with ProcessPoolExecutor() as executor:
        values = executor.map(process_seed_range_1, seed_ranges)
    return min(values)


def get_seed_ranges(seeds):
    result = []
    for i in range(0, len(seeds), 2):
        result.append((seeds[i], seeds[i]+seeds[i+1]))
    return result


def create_chunks(r, num_chunks):
    start, end = r
    chunks = []
    chunk_size = int((end - start) / num_chunks)
    while start <= end:
        chunk_start = start
        chunk_end = min(start + chunk_size, end)
        chunks.append((chunk_start, chunk_end))
        start = chunk_end + 1
    return chunks


def process_seed_range(arg, step):
    problem, seed_range = arg
    min_loc = float("inf")
    start, end = seed_range
    for seed in range(start, end + 1, step):
        n = seed
        for mapping in problem[1:]:
            n = map_next(n, mapping)
        if n < min_loc:
            min_loc = n
            print(min_loc)
    return min_loc


if __name__ == "__main__":
    main()
