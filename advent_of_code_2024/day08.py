from helper import load_input
import numpy as np
import itertools

# For each node type list all coordinates
# loop through each node type
    # itertools for pairs and none repeating e.g. not 11 12 and 12 11
    # check valid antinodes (i.e. on board)
    # if valid then add to total

def parse_input(contents):
    return np.array([list(line) for line in contents.strip().split('\n')])

def get_antenna_coordinates(array):
    symbol_dict = {}
    for symbol in np.unique(array):
        if symbol != '.':
            symbol_dict[symbol] = np.argwhere(array == symbol)
    return symbol_dict

def is_valid_coordinate(coord, puzzle_map):
    rows, cols = puzzle_map.shape
    row, col = coord
    return 0 <= row < rows and 0 <= col < cols

def part1(contents):
    puzzle_map = parse_input(contents)
    antenna_dict = get_antenna_coordinates(puzzle_map)
    total = 0
    for symbol, coords in antenna_dict.items():
        for coord1, coord2 in itertools.combinations(coords, 2):
            antinodes = get_antinode_coords(coord1, coord2)
            for antinode_coord in antinodes:
                if is_valid_coordinate(antinode_coord, puzzle_map):
                    total += 1

    return total

def part2(contents):
    pass


if __name__ == "__main__":

    test_input = load_input("day08_test").read()
    test_solution = part1(test_input)
    assert test_solution == 14, test_solution
    test_solution = part2(test_input)
    assert test_solution == None, test_solution

    puzzle_input = load_input("day08").read()
    puzzle_solution = part1(puzzle_input)
    print(f"Part1: {puzzle_solution}")
    puzzle_solution = part2(puzzle_input)
    print(f"Part2: {puzzle_solution}")
