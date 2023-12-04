from tasks.utils import get_nums_and_winners
from collections import defaultdict


def part_1(_input: str):
    res = 0
    for l in _input.splitlines():
        nums, winners = get_nums_and_winners(l)
        diff = sum(1 for i in winners if i in nums)
        total = 2 ** (diff - 1)
        res += total if diff > 0 else 0
    return res


def part_2(_input: str):
    d = defaultdict(int)
    for i, line in enumerate(_input.splitlines()):
        d[i] += 1
        nums, winners = get_nums_and_winners(line)
        for j in range(sum(1 for i in winners if i in nums)):
            d[i + 1 + j] += d[i]

    return sum(d.values())
