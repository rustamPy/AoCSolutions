def part_1(_input: str):
    res = 0
    for line in _input.splitlines():
        if line.startswith('+'):
            res += int(line[1:])
        else:
            res -= int(line[1:])
    return res
