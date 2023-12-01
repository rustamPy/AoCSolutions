def left_right_founder(s: str, reverse: bool) -> str:
    _map = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    # ls = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    if not reverse:
        for i in range(1, len(s) + 1):
            substr = s[:i]
            for k, v in _map.items():
                if s[i - 1].isdigit():
                    return s[i - 1]
                if k in substr:
                    return v
    else:
        for i in range(len(s) - 1, -1, -1):
            substr = s[i:len(s)]
            for k, v in _map.items():
                if s[i].isdigit():
                    return s[i]
                if k in substr:
                    return v

                """
                if number in substr:
                    return str(ind + 1)
                """
    return ''


def common_letters(word_1, word_2):
    return ''.join(c1 for c1, c2 in zip(word_1, word_2) if c1 == c2)
