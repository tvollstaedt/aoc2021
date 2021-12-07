from typing import List
from collections import Counter


def part1(input: List[str]):
    tank = []
    for fish in input[0].split(","):
        tank.append(int(fish))

    for day in range(0, 80):
        append = 0
        for idx, fish in enumerate(tank):
            if fish > 0:
                tank[idx] -= 1
            else:
                tank[idx] = 6
                append += 1

        for newfish in range(0, append):
            tank.append(8)

    return len(tank)


def part2(input: List[str]):
    ages = Counter([int(num) for num in input[0].split(',')])

    for day in range(256):
        for n in range(-1, 8):
            ages[n] = ages[n + 1]

        ages[8] = ages[-1]
        ages[6] += ages[-1]
        ages[-1] = 0

    return sum(ages.values())
