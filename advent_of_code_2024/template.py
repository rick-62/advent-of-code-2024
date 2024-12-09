from helper import load_input


def part1(contents):
    pass

def part2(contents):
    pass


if __name__ == "__main__":

    test_input = load_input("day00_test").read()
    test_solution = part1(test_input)
    assert test_solution == None, test_solution
    test_solution = part2(test_input)
    assert test_solution == None, test_solution

    puzzle_input = load_input("day00").read()
    puzzle_solution = part1(puzzle_input)
    print(f"Part1: {puzzle_solution}")
    puzzle_solution = part2(puzzle_input)
    print(f"Part2: {puzzle_solution}")
