from typing import List
from math import prod

def part1(input: List[str]):
    height_map = list(list(map(int, row)) for row in input)
    low_points = list(t[0] for t in get_low_points(height_map))
    return sum(map(lambda p: p + 1, low_points))


def get_low_points(height_map):
    low_points = []
    for x in range(0, len(height_map[0])):
        for y in range(0, len(height_map)):
            nb = [get(height_map, x, y + 1), get(height_map, x - 1, y), get(height_map, x, y - 1),
                  get(height_map, x + 1, y)]
            if height_map[y][x] < min(nb):
                low_points.append((height_map[y][x], x, y))
    return low_points


def get(height_map, x, y):
    if x < 0 or y < 0 or x > len(height_map[0]) - 1 or y > len(height_map) - 1:
        return 9
    return height_map[y][x]


def part2(input: List[str]):
    height_map = list(list(map(int, row)) for row in input)
    cols = len(height_map[0])
    rows = len(height_map)
    low_points = get_low_points(height_map)
    basins = []
    for point in low_points:
        basin_tmp = [point]
        basin = [point]
        while len(basin_tmp) > 0:
            curr = basin_tmp.pop(0)
            # go + horizontal
            for x_diff in range(1, cols):
                num = get(height_map, curr[1] + x_diff, curr[2])
                if num == 9:
                    break
                bas = (num, curr[1] + x_diff, curr[2])
                if bas in basin:
                    break
                basin.append(bas)
                basin_tmp.append(bas)

            # go - horizontal
            for x_diff in range(1, cols):
                num = get(height_map, curr[1] - x_diff, curr[2])
                if num == 9:
                    break
                bas = (num, curr[1] - x_diff, curr[2])
                if bas in basin:
                    break
                basin.append(bas)
                basin_tmp.append(bas)

            # go + vertically
            for y_diff in range(1, rows):
                num = get(height_map, curr[1], curr[2] + y_diff)
                if num == 9:
                    break
                bas = (num, curr[1], curr[2] + y_diff)
                if bas in basin:
                    break
                basin.append(bas)
                basin_tmp.append(bas)

            # go - vertically
            for y_diff in range(1, rows):
                num = get(height_map, curr[1], curr[2] - y_diff)
                if num == 9:
                    break
                bas = (num, curr[1], curr[2] - y_diff)
                if bas in basin:
                    break
                basin.append(bas)
                basin_tmp.append(bas)
        basins.append(basin)

    return prod(sorted(list(map(len, basins)), reverse=True)[0:3])
