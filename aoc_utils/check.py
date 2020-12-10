import sys
import aocd.runner


def check(args):
    year = args[1]
    day = args[2]
    print("Checking solution for puzzle {} {}".format(year, day))
    sys.argv = [sys.argv[0], "-d", day, "-y", year]
    aocd.runner.main()


def main():
    check(sys.argv)


if __name__ == "__main__":
    main()
