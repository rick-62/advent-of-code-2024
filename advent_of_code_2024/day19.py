from helper import load_input
from itertools import product
import math
from functools import lru_cache

def parse_input(input_str):
    parts = input_str.strip().split('\n\n', 1)
    first_part = parts[0].split(', ')
    second_part = parts[1].split('\n')
    return first_part, second_part

@lru_cache(maxsize=None)
def is_valid_design(patterns, design):
    for pattern in patterns:
        if pattern == design:
            return True
        elif design.startswith(pattern):
            if is_valid_design(tuple(patterns), design[len(pattern):]):
                return True
            else:
                continue
    return False

@lru_cache(maxsize=None)
def count_pattern_combinations(patterns, design, counter=0):
    for pattern in patterns:
        if pattern == design:
            counter += 1
        elif design.startswith(pattern):
            counter += count_pattern_combinations(tuple(patterns), design[len(pattern):])
    return counter

def part1(contents):
    patterns, designs = parse_input(contents)
    valid_designs = [d for d in designs if is_valid_design(tuple(patterns), d)]
    return len(valid_designs)

def part2(contents):
    patterns, designs = parse_input(contents)
    valid_designs = [d for d in designs if is_valid_design(tuple(patterns), d)]
    total = 0
    for design in valid_designs:
        total += count_pattern_combinations(tuple(patterns), design)
    return total


if __name__ == "__main__":

    test_input = load_input("day19_test").read()
    test_solution = part1(test_input)
    assert test_solution == 6, test_solution
    test_solution = part2(test_input)
    assert test_solution == 16, test_solution

    puzzle_input = load_input("day19").read()
    puzzle_solution = part1(puzzle_input)
    print(f"Part1: {puzzle_solution}")
    puzzle_solution = part2(puzzle_input)
    print(f"Part2: {puzzle_solution}")
