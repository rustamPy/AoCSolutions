def run_task(year: str = '', day: str = '', part: str = '', inp: str = ''):
    module_name = f"tasks.{year}.day_{day}_solutions"
    function_name = f"part_{part}"

    try:
        module = __import__(module_name, fromlist=[function_name])
        func = getattr(module, function_name)
        return func(inp)

    except ImportError:
        print(
            f"Module -> tasks.{year}.day_{day}_solutions not found - the day didn't come yet"
        )

    except AttributeError:
        print(
            f"Function -> part_{part} not found in tasks.{year}.day_{day}_solutions - "
            f"didn't complete the part {part} yet"
        )


if __name__ == "__main__":
    YEAR_INPUT = input("Enter year (2023 is default): ")
    DAY_INPUT = input("Enter day number (1 is default): ")
    PART_INPUT = input("Enter part number (1 is default): ")

    if not YEAR_INPUT or len(YEAR_INPUT) < 4:
        YEAR_INPUT = '2023'

    if not DAY_INPUT or DAY_INPUT not in map(str, range(1, 26)):
        DAY_INPUT = '1'

    if not PART_INPUT or PART_INPUT not in map(str, [1, 2]):
        PART_INPUT = '1'

    INP_TYPE = input("Is your input a file? (y/n) (y is default): ").lower()

    if not INP_TYPE and INP_TYPE not in ['y', 'n']:
        INP_TYPE = 'y'

    INPUT_STR = ''
    REPLIT_PATH = 'https://replit.com/@rustamPy/AoCSolutions#'
    INPUT_PATH = f'inputs/{YEAR_INPUT}/day_{DAY_INPUT}_input.txt'
    if INP_TYPE == "y":
        try:
            with open(INPUT_PATH, "r") as f:
                INPUT_STR = f.read()
        except FileNotFoundError:
            print(f"No input for {YEAR_INPUT}-December-{DAY_INPUT}")

    else:
        INPUT_STR = input("Enter string input: ")

    print('--------------------------------------------')
    if INP_TYPE == "y":
        print(f'INPUT PATH: {REPLIT_PATH}{INPUT_PATH}')
    else:
        print(f'YOUR INPUT: {INPUT_STR}')
    print('--------------------------------------------')
    print(
        f"THE ANSWER IS: {run_task(YEAR_INPUT, DAY_INPUT, PART_INPUT, INPUT_STR)}"
    )
    print('--------------------------------------------')
