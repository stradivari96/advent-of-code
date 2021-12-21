import copy


def part_1(draws, boards):
    boards = copy.deepcopy(boards)
    for number in draws:
        for board in boards:
            for i in range(len(board)):
                for j in range(len(board)):
                    if board[i][j] == number:
                        board[i][j] = None
                    if _check_row(board, i) or _check_col(board, j):
                        return _get_score(board) * number


def _check_row(board, row):
    return all(board[row][j] is None for j in range(len(board)))


def _check_col(board, col):
    return all(board[i][col] is None for i in range(len(board)))


def _get_score(board):
    return sum(sum(i for i in row if i is not None) for row in board)


def part_2(draws, boards):
    boards = copy.deepcopy(boards)
    won = set()
    for number in draws:
        for idx, board in enumerate(boards):
            if idx in won:
                continue
            for i in range(len(board)):
                for j in range(len(board)):
                    if board[i][j] == number:
                        board[i][j] = None
                    if _check_row(board, i) or _check_col(board, j):
                        won.add(idx)
                    if len(boards) == len(won):
                        return _get_score(board) * number


if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.read().split("\n\n")
    draws = [int(i) for i in data[0].split(",")]
    boards = []
    for board in data[1:]:
        board = board.split("\n")
        board_ = []
        for row in board:
            board_.append([int(i) for i in row.split()])
        boards.append(board_)

    print(part_1(draws, boards))
    print(part_2(draws, boards))
