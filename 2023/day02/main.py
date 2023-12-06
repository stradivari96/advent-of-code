from collections import defaultdict

def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    games_by_id = {}
    for line in lines:
        game_id, games = line.split(": ")
        game_id = int(game_id.replace("Game ", ""))
        games = games.split("; ")
        games_by_id[game_id] = [g.split(", ") for g in games]
    print(part_1(games_by_id))
    print(part_2(games_by_id))


def part_1(games):
    limit = {"red": 12, "green": 13, "blue": 14}
    total = 0
    for game_id, game in games.items():
        valid_game = True
        for game_set in game:
            count = defaultdict(int)
            for draw in game_set:
                val, color = draw.split(" ")
                count[color] += int(val)
                for color, val in count.items():
                    if val > limit[color]:
                        valid_game = False
        if valid_game:
            total += game_id
    return total


def part_2(games):
    total = 0
    for game in games.values():
        min_color = {"red": 0, "green": 0, "blue": 0}
        for game_set in game:
            for draw in game_set:
                val, color = draw.split(" ")
                min_color[color] = max(int(val), min_color[color])
        power = 1
        for n in min_color.values():
            power *= n
        total += power
    return total


if __name__ == "__main__":
    main()
