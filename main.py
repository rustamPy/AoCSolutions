def run_task(year: str = '', day: str = '', part: str = '', input: str = ''):
    module_name = f"tasks.{year}.day_{day}_solutions"
    function_name = f"part_{part}"

    try:
        module = __import__(module_name, fromlist=[function_name])
        func = getattr(module, function_name)
        return func(input)

    except ImportError:
        print(
            f"Module -> tasks.{year}.day_{day}_solutions not found - the day didn't come yet"
        )

    except AttributeError:
        print(
            f"Function -> part_{part} not found in tasks.{year}.day_{day}_solutions - didn't complete the part {part} yet"
        )


if __name__ == "__main__":
    year_input = input("Enter year (2023 is default): ")
    day_input = input("Enter day number (1 is default): ")
    part_input = input("Enter part number (1 is default): ")

    if not year_input or len(year_input) < 4:
        year_input = '2023'

    if not day_input or day_input not in map(str, range(1, 26)):
        day_input = '1'

    if not part_input or part_input not in map(str, [1, 2]):
        part_input = '1'

    inp_type = input("Is your input a file? (y/n) (y is default): ").lower()

    if not inp_type and inp_type not in ['y', 'n']:
        inp_type = 'y'

    input_str = ''
    if inp_type == "y":
        try:
            with open(f"inputs/{year_input}/day_{day_input}_input.txt", "r") as f:
                input_str = f.read()
        except FileNotFoundError:
            print(f"No input for {year_input}-December-{day_input}")



    else:
        input_str = input("Enter string input: ")

    print('--------------------------------------------')
    print(f'INPUT: {input_str}')
    print('--------------------------------------------')
    print(f"THE ANSWER IS: {run_task(year_input, day_input, part_input, input_str)}")
    print('--------------------------------------------')
