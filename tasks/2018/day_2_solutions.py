from tasks.utils import common_letters


def part_1(_input: str):
    _map = [0, 0]
    for line in _input.splitlines():
        all_letters = set(line)
        checker = []
        if len(all_letters) == line:
            continue
        for letter in all_letters:
            c = line.count(letter)
            if c == 2 and 2 not in checker:
                _map[0] += 1
                checker.append(2)
            elif c == 3 and 3 not in checker:
                _map[1] += 1
                checker.append(3)
    return _map[0] * _map[1]


def part_2(_input: str):
    diff = len(_input.splitlines()[0])
    len_w = len(_input.splitlines()[0])
    res = []
    for i, i_word in enumerate(_input.splitlines()):
        for j, j_word in enumerate(_input.splitlines()):
            if i != j:
                curr_diff = sum(c1 != c2 for c1, c2 in zip(i_word, j_word))
                if curr_diff == len_w:
                    continue
                diff = min(curr_diff, diff)
                if curr_diff == diff:
                    res.append(common_letters(i_word, j_word))
    return res[-1]
