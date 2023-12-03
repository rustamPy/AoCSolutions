from math import prod
from collections import defaultdict


def part_1(_input: str) -> int:
    return calculator(_input.splitlines())[0]


def part_2(_input: str) -> int:
    inp = _input.splitlines()
    gears = calculator(inp)[1]
    return sum(prod(gear) for gear in gears.values() if len(gear) == 2)


def calculator(inp) -> tuple:
    # building a data with coordinates
    data = {x + 1j * y: c for x, line in enumerate(inp) for y, c in enumerate(line)}

    # just a random line (can be any since they are all same)
    one_line = inp[-1]

    # initialize result
    res = 0

    # gears dd
    gears = defaultdict(list)
    for x in range(len(inp)):
        num = ''
        valid = False
        gear_position = None

        for y in range(len(one_line)):
            c = data[x + 1j * y]
            if c.isdigit():
                # build a number
                num += c
                if not valid:
                    # check what's around the current digit char
                    """
                    {0+0j: '.'}, {0+1j: '.'}, {0+2j: '.'}
                    {1+0j: '.'}, {1+1j: '7'}, {1+2j: '.'}
                    {2+0j: '#'}, {2+1j: '.'}, {2+2j: '.'}
                    
                    if c is digit -> {1+1j: '7'}
                    
                    it will check what is around the current coordinates {1+1j}
                    around means (left, right, up, down + 4 diagonal sides + center (ignored)):
                    SW - (-1, -1)
                    W - (-1, 0)
                    WN - (-1, 1)
                    S - (0, -1)
                    CENTER (itself) - (0, 0) 
                    N - (0, 1)
                    SE - (1, -1)
                    E - (1, 0)
                    NE - (1, 1)
                    """
                    for x1 in range(-1, 2):
                        for y1 in range(-1, 2):
                            # new coefficients (x1, y1) based on the existing (x, y) coordinates
                            coord = x + x1 + 1j * (y + y1)

                            surround = data.get(coord, '.')
                            # if there is a digit around (itself included) and values other than '.' (dot)
                            if not surround.isdigit() and surround != '.':

                                # then consider valid
                                valid = True

                                # for part 2 - if exactly asterisk (gear icon)
                                if surround == '*':
                                    gear_position = coord
            else:
                # we end up here when inspecting value is not digit

                # if valid is turned on (if there were number which was surrounded by symbols)
                if valid:

                    # convert string to int f.e. '431' -> 431
                    n = int(num)

                    # increment result by this number
                    res += n

                    # if gear position is equals to coordinate (not None, which is default)
                    if gear_position:
                        # append the number to default dict by coordinate key
                        gears[gear_position].append(n)

                    # switch off valid again
                    valid = False

                    # switch off gear position again
                    gear_position = None
                num = ''

        # for the last one
        if valid:
            n = int(num)
            res += n
            if gear_position:
                gears[gear_position].append(n)

    return res, gears
