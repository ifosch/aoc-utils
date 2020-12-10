import sys
import pytest


def run_tests(args):
    year = args[1]
    day = int(args[2])
    print("Running tests for puzzle {} {}".format(year, day))
    pytest.main(["-v", "aoc/aoc{}/test_q{:02d}.py".format(year, day)])


def main():
    run_tests(sys.argv)


if __name__ == "__main__":
    main()
