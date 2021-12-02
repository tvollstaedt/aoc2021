from typing import List


def part1(input: List[str]):
    prev = None
    increases = 0
    for i in input:
        if prev is None:
            prev = 0
            continue

        if prev < int(i):
            increases += 1

        prev = int(i)
    return increases


def part2(input: List[str]):
    p = 0
    increases = 0
    prevsum = None
    while p + 2 < len(input):
        if prevsum is None:
            prevsum = 0
            p += 1
            continue

        prevsum = int(input[p - 1]) + int(input[p]) + int(input[p + 1])
        cursum = int(input[p + 0]) + int(input[p + 1]) + int(input[p + 2])
        if prevsum < cursum:
            increases += 1

        p += 1

    return increases
