from typing import List

import numpy


def part1(input: List[str]):
    return bingo(input)[0]


def part2(input: List[str]):
    return bingo(input)[-1]


def bingo(input: List[str]):
    boards = [[]]
    num = 0

    # read numbers
    numbers = list(map(int, input[0].split(",")))

    # read boards
    for line in input[2:]:
        if line == "":
            num += 1
            boards.append([])
            continue

        boards[num].append(list(map(int, line.split())))

    wins = []
    boardnum = len(boards)
    skipboards = []

    # mark numbers in boards
    for number in numbers:
        for boardidx, board in enumerate(boards):
            for row in board:
                if not boardidx in skipboards and number in row:
                    idx = row.index(number)
                    row[idx] = 0
                    # check for winning board
                    if check_win(board):
                        boardsum = sum(map(sum, board))
                        wins.append(boardsum * number)
                        if len(wins) == boardnum:
                            return wins
                        skipboards.append(boardidx)

    return wins


def check_win(board):
    for row in range(5):
        if sum(board[row]) == 0:
            return True

    colsums = [sum(col) for col in zip(*board)]
    for col in range(5):
        if colsums[col] == 0:
            return True

    return False
