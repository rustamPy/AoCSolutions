from math import prod
from time import time


def parse(_input: str):
    return [[int(j) for j in i.split() if j.isdigit()] for i in _input.splitlines()]


def part_1(_input):
    hit = 0
    res = 1
    for t, d in zip(*parse(_input)):
        for ms in range(1, t + 1):
            current_d = ms * (t - ms)
            if current_d > d:
                hit += 1
            elif hit:
                res *= hit
                hit = 0
                break
    return res


def part_2(_input):
    t, d = [int(''.join(map(str, subarray))) for subarray in parse(_input)]
    hit = 0
    for ms in range(1, t + 1):
        current_d = ms * (t - ms)
        if current_d > d:
            hit += 1
        elif hit:
            return hit


def part_1_alternative(_input):
    return prod([len([i * (t - i) for i in range(1, t + 1) if i * (t - i) > d]) for t, d in zip(*parse(_input))])


def part_2_alternative(_input):
    t, d = [int(''.join(map(str, subarray))) for subarray in parse(_input)]
    return len([i * (t - i) for i in range(1, t + 1) if i * (t - i) > d])
