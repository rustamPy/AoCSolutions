def part_1(_input: str):
    res, s = 0, 0
    for line in _input.splitlines():
        # line is empty/break point
        if not line:
            res = max(res, s)
            s = 0

        # if line is digit string
        else:
            s += int(line)
    return res


def part_2(_input: str):
    res, s = [], 0
    for line in _input.splitlines():
        # line is empty/break point
        if not line:
            res.append(s)
            s = 0
        # if line is digit string
        else:
            s += int(line)
    return sum(sorted(res)[-3:])
