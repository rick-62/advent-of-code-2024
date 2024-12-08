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

def get_antinode_coords(coord1, coord2):
    row1, col1 = coord1
    row2, col2 = coord2
    
    # Calculate the differences
    row_diff = row2 - row1
    col_diff = col2 - col1
    
    # Calculate the antinode coordinates
    antinode1 = (row1 - row_diff, col1 - col_diff)
    antinode2 = (row2 + row_diff, col2 + col_diff)
    
    return [antinode1, antinode2]


def part1(contents):
    puzzle_map = parse_input(contents)
    antenna_dict = get_antenna_coordinates(puzzle_map)
    antinode_locations = set()
    for symbol, coords in antenna_dict.items():
        for coord1, coord2 in itertools.combinations(coords, 2):
            antinodes = get_antinode_coords(coord1, coord2)
            for antinode_coord in antinodes:
                if is_valid_coordinate(antinode_coord, puzzle_map):
                    antinode_locations.add(antinode_coord)

    return len(antinode_locations)

def get_antinode_coords_part2(coord1, coord2, puzzle_map):
    row1, col1 = coord1
    row2, col2 = coord2
    
    # Calculate the differences
    row_diff = row2 - row1
    col_diff = col2 - col1
    
    antinodes = [(row1, col1), (row2, col2)]
    
    # Generate antinodes in the negative direction
    current_row, current_col = row1, col1
    while True:
        current_row -= row_diff
        current_col -= col_diff
        if is_valid_coordinate((current_row, current_col), puzzle_map):
            antinodes.append((current_row, current_col))
        else:
            break
    
    # Generate antinodes in the positive direction
    current_row, current_col = row2, col2
    while True:
        current_row += row_diff
        current_col += col_diff
        if is_valid_coordinate((current_row, current_col), puzzle_map):
            antinodes.append((current_row, current_col))
        else:
            break
    
    return antinodes

def part2(contents):
    puzzle_map = parse_input(contents)
    antenna_dict = get_antenna_coordinates(puzzle_map)
    antinode_locations = set()
    for symbol, coords in antenna_dict.items():
        for coord1, coord2 in itertools.combinations(coords, 2):
            antinodes = get_antinode_coords_part2(coord1, coord2, puzzle_map)
            for antinode_coord in antinodes:
                if is_valid_coordinate(antinode_coord, puzzle_map):
                    antinode_locations.add(antinode_coord)

    return len(antinode_locations)


if __name__ == "__main__":

    test_input = load_input("day08_test").read()
    test_solution = part1(test_input)
    assert test_solution == 14, test_solution
    test_solution = part2(test_input)
    assert test_solution == 34, test_solution

    puzzle_input = load_input("day08").read()
    puzzle_solution = part1(puzzle_input)
    print(f"Part1: {puzzle_solution}")
    puzzle_solution = part2(puzzle_input)
    print(f"Part2: {puzzle_solution}")
