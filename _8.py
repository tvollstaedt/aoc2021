from typing import List


def part1(input: List[str]):
    digcount = 0

    for line in input:
        digits = line.split(" | ")[1].split()
        digcount += len([dig for dig in digits if len(dig) in [2, 4, 3, 7]])

    return digcount


def part2(input: List[str]):
    sum = 0
    for line in input:
        segments, digits = map(lambda x: x.split(), line.split(" | "))

        seg_map = {}
        num_map = {number: find_seg(segments, number) for number in range(0, 10)}

        # retrieve a from 7
        seg_map['a'] = set(num_map[7][0]).difference(num_map[1][0]).pop()

        # find 3, deduct 2 and 5
        num_map[3] = list(filter(lambda s: set(num_map[1][0]).issubset(s), num_map[3]))
        num_map[2] = [x for x in num_map[2] if x != num_map[3][0]]
        num_map[5] = [x for x in num_map[5] if x != num_map[3][0]]

        # get g mapping from 3 - 4 - a
        seg_map['g'] = set(num_map[3][0]).difference(num_map[4][0])
        seg_map['g'].remove(seg_map['a'])
        seg_map['g'] = seg_map['g'].pop()

        # get d mapping from 3 - 1 - a - g
        seg_map['d'] = set(num_map[3][0]).difference(num_map[1][0])
        seg_map['d'].remove(seg_map['a'])
        seg_map['d'].remove(seg_map['g'])
        seg_map['d'] = seg_map['d'].pop()

        # get b mapping by 4 - 1 - d
        seg_map['b'] = set(num_map[4][0]).difference(num_map[1][0])
        seg_map['b'].remove(seg_map['d'])
        seg_map['b'] = seg_map['b'].pop()

        # find e mapping from 5 - 2 - 1 - 3
        seg_map['e'] = set(num_map[2][0]).symmetric_difference(num_map[2][1]).difference(num_map[1][0])
        seg_map['e'].remove(seg_map['b'])
        seg_map['e'] = seg_map['e'].pop()

        # find 2 and 5
        num_map[2] = list(filter(lambda s: seg_map['e'] in s, num_map[2]))
        num_map[5] = list(filter(lambda s: seg_map['b'] in s, num_map[5]))

        # get c mapping from 2 by map all others
        two = set(num_map[2][0])
        for char in ['a', 'd', 'e', 'g']:
            two.remove(seg_map.get(char))
        seg_map['c'] = two.pop()

        # get f mapping from 1 - c
        seg_map['f'] = set(num_map[1][0])
        seg_map['f'].remove(seg_map['c'])
        seg_map['f'] = seg_map['f'].pop()

        # find 0
        num_map[0] = list(filter(
            lambda num: 0 not in [seg_map[c] in num for c in list('abcefg')], num_map[0]))

        # find 6
        num_map[6] = list(filter(
            lambda num: 0 not in [seg_map[c] in num for c in list('abdefg')], num_map[6]))

        # find 6
        num_map[9] = list(filter(
            lambda num: 0 not in [seg_map[c] in num for c in list('abcdfg')], num_map[9]))

        # remap
        num_map = {v[0]: k for k, v in num_map.items()}

        # convert digits
        output = ""
        for digit in digits:
            output += str(num_map.get([k for k, v in num_map.items() if sorted(digit) == sorted(k)][0]))
        sum += int(output)

    return sum


def find_seg(segments: List[str], number: int):
    decoder = {
        0: lambda: [seg for seg in segments if len(seg) == 6],
        1: lambda: [seg for seg in segments if len(seg) == 2],
        2: lambda: [seg for seg in segments if len(seg) == 5],
        3: lambda: [seg for seg in segments if len(seg) == 5],
        4: lambda: [seg for seg in segments if len(seg) == 4],
        5: lambda: [seg for seg in segments if len(seg) == 5],
        6: lambda: [seg for seg in segments if len(seg) == 6],
        7: lambda: [seg for seg in segments if len(seg) == 3],
        8: lambda: [seg for seg in segments if len(seg) == 7],
        9: lambda: [seg for seg in segments if len(seg) == 6]
    }

    segment = decoder.get(number)

    return segment() if segment else None
