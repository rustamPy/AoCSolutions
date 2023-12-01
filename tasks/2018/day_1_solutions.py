def part_1(_input: str):
    return sum(int(x) for x in _input.splitlines())


def part_2(_input: str):
    ls = {0}
    res = 0
    while True:
        for line in _input.splitlines():
            res += int(line)
            if res in ls:
                return res
            ls.add(res)