def part_1(_input: str):
    res = 0
    for line in _input.splitlines():
        res = res + int(line[1:]) if line.startswith('+') else res - int(line[1:])
    return res
