from typing import List


def part1(input: List[str]):
    points = {}
    for line in input:
        x, y = line.split(" -> ")
        x1, y1 = list(map(int, x.split(",")))
        x2, y2 = list(map(int, y.split(",")))

        if x1 == x2:
            step = 1 if y1 <= y2 else -1

            for i in range(y1, y2 + step, step):
                point = str(x1) + "," + str(i)
                if not point in points:
                    points[point] = 1
                else:
                    points[point] += 1
        elif y1 == y2:
            step = 1 if x1 <= x2 else -1

            for i in range(x1, x2 + step, step):
                point = str(i) + "," + str(y1)
                if not point in points:
                    points[point] = 1
                else:
                    points[point] += 1

    counter = 0
    for key, value in points.items():
        if value >= 2:
            counter += 1

    return counter


def part2(input: List[str]):
    points = {}
    for line in input:
        x, y = line.split(" -> ")
        x1, y1 = list(map(int, x.split(",")))
        x2, y2 = list(map(int, y.split(",")))

        # Horizontal line
        if x1 == x2:
            step = 1 if y1 <= y2 else -1

            for i in range(y1, y2 + step, step):
                point = str(x1) + "," + str(i)
                if not point in points:
                    points[point] = 1
                else:
                    points[point] += 1

        # Vertical line
        elif y1 == y2:
            step = 1 if x1 <= x2 else -1

            for i in range(x1, x2 + step, step):
                point = str(i) + "," + str(y1)
                if not point in points:
                    points[point] = 1
                else:
                    points[point] += 1

        # Diagonal line
        else:
            step_x = 1 if x1 <= x2 else -1
            step_y = 1 if y1 <= y2 else -1

            for i in range(0, abs(x1 - x2) + 1):
                point = str(x1 + step_x * i) + "," + str(y1 + step_y * i)
                if not point in points:
                    points[point] = 1
                else:
                    points[point] += 1

    counter = 0
    for key, value in points.items():
        if value >= 2:
            counter += 1

    return counter

