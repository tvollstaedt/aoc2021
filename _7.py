from typing import List


def part1(input: List[str]):
    crabs = [int(i) for i in input[0].split(",")]
    max_pos = max(crabs)
    fuels = [0] * max_pos
    for pos in range(0, max_pos):
        for crab in crabs:
            fuels[pos] += abs(crab - pos)

    return min(fuels)


def part2(input: List[str]):
    crabs = [int(i) for i in input[0].split(",")]
    max_pos = max(crabs)
    fuels = []
    last_cost = -1

    for pos in range(0, max_pos):
        fuels.append(0)

        for crab in crabs:
            for cost in range(0, abs(crab - pos) + 1):
                fuels[pos] += cost
        if -1 < last_cost < fuels[pos]:
            break  # skip higher values
        last_cost = fuels[pos]

    return min(fuels)
