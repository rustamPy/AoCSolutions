from tasks.utils import get_nums_and_winners
from collections import defaultdict

"""
Sample input:
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11

"""
def part_1(_input: str):
    res = 0
    for l in _input.splitlines():
        nums, winners = get_nums_and_winners(l)
        matches = len(nums & winners)
        points = 2 ** (matches - 1)
        res += points if matches > 0 else 0
    return res


def part_2(_input: str):
    d = defaultdict(int)
    for i, line in enumerate(_input.splitlines()):
        d[i] += 1
        nums, winners = get_nums_and_winners(line)
        for j in range(sum(1 for i in winners if i in nums)):
            d[i + 1 + j] += d[i]

    return sum(d.values())
