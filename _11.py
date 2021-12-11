from typing import List


def part1(input: List[str]):
    counter = {
        'flashes': 0
    }
    octopus_map = list(list(map(int, row)) for row in input)
    for step in range(0, 100):
        octopus_map = [[col + 1 for col in row] for row in octopus_map]
        octopus_map = flash(octopus_map, counter)

    return counter['flashes']


def flash(octopus_map, counter):
    flash_map = list(map(lambda e: e[0], filter(lambda e: len(e) > 0,
                                                [[(i, j) for j, col in enumerate(row) if col == 10] for i, row in
                                                 enumerate(octopus_map)])))
    if len(flash_map) == 0:
        # Set marked entities to 0
        for i, row in enumerate(octopus_map):
            for j, _ in enumerate(row):
                if octopus_map[i][j] == -1:
                    counter["flashes"] += 1
                    octopus_map[i][j] = 0
        return octopus_map
    else:
        for row_index, col_index in flash_map:
            octopus_map[row_index][col_index] = -1
            for x, y in [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]:
                octopus_map = inc(octopus_map, col_index + x, row_index + y)
        return flash(octopus_map, counter)


def inc(octopus_map, x, y):
    if x < 0 or y < 0 or x > len(octopus_map[0]) - 1 or y > len(octopus_map) - 1 or octopus_map[y][x] == 10 or \
            octopus_map[y][x] == -1:
        return octopus_map
    octopus_map[y][x] += 1
    return octopus_map


def part2(input: List[str]):
    counter = {
        'flashes': 0
    }
    octopus_map = list(list(map(int, row)) for row in input)
    for step in range(0, 999999):
        if sum(sum(octopus_map, [])) == 0:
            return step
        octopus_map = [[col + 1 for col in row] for row in octopus_map]
        octopus_map = flash(octopus_map, counter)
