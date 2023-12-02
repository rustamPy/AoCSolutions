from typing import Tuple


def builder(line: str) -> Tuple[dict, str]:
    s = {"red": 0, 'green': 0, 'blue': 0}
    data = ''.join(line.split("Game ")).split(' ')
    for i in range(2, len(data)):
        if 'green' in data[i]:
            s['green'] = max(int(data[i - 1]), s['green'])
        elif 'blue' in data[i]:
            s['blue'] = max(int(data[i - 1]), s['blue'])
        elif 'red' in data[i]:
            s['red'] = max(int(data[i - 1]), s['red'])
    return s, data


def part_1(_input: str):
    res = 0
    for line in _input.splitlines():
        s = builder(line)[0]
        data = builder(line)[1]
        if s['red'] <= 12 and s['green'] <= 13 and s['blue'] <= 14:
            res += int(data[0][:-1])

    return res


def part_2(_input: str):
    res = 0
    for line in _input.splitlines():
        s = builder(line)[0]
        res += s['red'] * s['green'] * s['blue']

    return res
