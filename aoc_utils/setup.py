import sys
import os
from pathlib import Path

def get_module_name(year):
    return os.path.join(os.getcwd(), "aoc", "aoc{}".format(year))


def get_module_path(module_name):
    return os.path.join("aoc", module_name)


def init_module(year):
    module_path = get_module_path(get_module_name(year))
    try:
        os.mkdir(module_path)
    except FileExistsError:
        pass
    Path(os.path.join(module_path, "__init__.py")).touch()
    return module_path


def init_puzzle(year, day):
    module_path = init_module(year)
    puzzle_code = """def part1(data):
    return 0


def part2(data):
    return 0


def solution(data):
    return part1(data), part2(data)
"""
    with open(os.path.join(module_path, "q{:02d}.py".format(int(day))), "w") as f:
              f.write(puzzle_code)


def setup(args):
    year = args[1]
    day = args[2]
    print("Setting up for puzzle {} {}".format(year, day))
    init_puzzle(year, day)


def main():
    setup(sys.argv)


if __name__ == "__main__":
    main()
