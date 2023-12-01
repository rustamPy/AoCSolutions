from tasks.utils import left_right_founder


def part_1(_input: str):
  res = 0
  for line in _input.splitlines():

    digits = []
    for char in line:
      if char.isdigit():
        digits.append(char)
    res += int(digits[0] + digits[-1])
  return res


def part_2(_input: str):
  res = 0
  for i in _input.splitlines():
    left = left_right_founder(i, False)
    right = left_right_founder(i, True)
    res += int(left + right)
  return res
