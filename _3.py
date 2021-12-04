from typing import List


def part1(input: List[str]):
    g, e = ["", ""]
    l = len(input[0])
    for i in range(0, l):
        p = 0
        n = 0

        for line in input:
            if line[i] == "1":
                p += 1
            else:
                n += 1
        if p > n:
            g += "1"
            e += "0"
        else:
            g += "0"
            e += "1"

    return int(g, 2) * int(e, 2)


def part2(input: List[str]):
    co2 = int(calc(input, 0, "oxy"), 2)
    oxy = int(calc(input, 0, "co2"), 2)
    return co2 * oxy


def calc(input: List[str], index, type):
    l = len(input[0])
    if len(input) == 1:
        return input[0]

    p = 0
    n = 0

    for line in input:
        if line[index] == "1":
            p += 1
        else:
            n += 1

    mcb = list(filter(lambda y: y[index] == "1", input))
    lcb = list(filter(lambda y: y[index] == "0", input))

    if type == "oxy":
        if p >= n:
            return calc(mcb, index + 1, type)
        else:
            return calc(lcb, index + 1, type)
    else:
        if n <= p:
            return calc(lcb, index + 1, type)
        else:
            return calc(mcb, index + 1, type)
