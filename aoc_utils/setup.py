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
    test_code = """import pytest

from aoc.aoc{} import q{:02d}


@pytest.mark.parametrize(
    "input, expected",
    [
        ("", (0, 0)),
        ("(", (1, 0)),
    ],
)
def test_q{:02d}(input, expected):
    assert q{:02d}.solution(input) == expected
""".format(year, day, day, day)
    with open(os.path.join(module_path, "test_q{:02d}.py".format(day)), "w") as f:
              f.write(test_code)
    puzzle_code = """def part1(data):
    return 0


def part2(data):
    return 0


def solution(data):
    return part1(data), part2(data)
"""
    with open(os.path.join(module_path, "q{:02d}.py".format(day)), "w") as f:
              f.write(puzzle_code)


def setup(args):
    year = args[1]
    day = int(args[2])
    print("Setting up for puzzle {} {}".format(year, day))
    init_puzzle(year, day)


def main():
    setup(sys.argv)


if __name__ == "__main__":
    main()
