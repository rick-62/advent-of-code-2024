import re
from helper import load_input

def part1(contents):
    # Regular expression to find all "mul" functions with two numbers
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, contents)
    
    total_sum = 0
    for match in matches:
        num1, num2 = map(int, match)
        total_sum += num1 * num2
    
    return total_sum

if __name__ == "__main__":
    test_input = load_input('day03_test').read()
    test_solution = part1(test_input)
    assert test_solution == 161, test_solution

    puzzle_input = load_input('day03').read()
    puzzle_solution = part1(puzzle_input)
    print(puzzle_solution)