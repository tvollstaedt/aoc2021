from typing import List


def part1(input: List[str]):
    x, y = [0, 0]
    for line in input:
        direction, amount = line.split()
        amount = int(amount)
        if direction == 'forward':
            x += amount
        elif direction == 'down':
            y += amount
        elif direction == 'up':
            y -= amount

    return x * y


def part2(input: List[str]):
    x, y, aim = [0, 0, 0]
    for line in input:
        direction, amount = line.split()
        amount = int(amount)
        if direction == 'forward':
            x += amount
            y += amount * aim
        elif direction == 'down':
            aim += amount
        elif direction == 'up':
            aim -= amount

    return x * y

