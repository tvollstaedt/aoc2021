import statistics
from typing import List

char_dict = {
    '{': '}', '(': ')', '[': ']', '<': '>'
}


def part1(input: List[str]):
    score = 0
    scores = {
        ')': 3, ']': 57, '}': 1197, '>': 25137
    }

    stack = []
    for line in input:
        for char in line:
            if char in char_dict.keys():
                stack.append(char)
            else:
                last = stack.pop()
                if not char_dict[last] == char:
                    score += scores[char]
                    break

    return score


def part2(input: List[str]):
    scores = {
        ')': 1, ']': 2, '}': 3, '>': 4
    }

    score_list = []
    for line in input:
        score = 0
        stack = []
        for idx, char in enumerate(line):
            if char in char_dict.keys():
                stack.append(char)
            else:
                last = stack.pop()
                if not char_dict[last] == char:
                    break

            if idx == len(line) - 1:  # finish incomplete line
                while len(stack) > 0:
                    last = stack.pop()
                    closer = char_dict[last]
                    score = score * 5 + scores[closer]
        if score > 0:
            score_list.append(score)
    return statistics.median(score_list)
