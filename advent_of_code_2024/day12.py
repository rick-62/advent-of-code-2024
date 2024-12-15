import numpy as np
from helper import load_input

def convert_to_2d_array(input_string):
    rows = input_string.strip().split('\n')
    array = np.array([list(row) for row in rows])
    return array

def flood_fill(array, x, y, visited, region):
    rows, cols = array.shape
    stack = [(x, y)]
    element = array[x, y]
    
    while stack:
        cx, cy = stack.pop()
        if (cx, cy) in visited:
            continue
        visited.add((cx, cy))
        region.append((cx, cy))
        
        for nx, ny in [(cx-1, cy), (cx+1, cy), (cx, cy-1), (cx, cy+1)]:
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and array[nx, ny] == element:
                stack.append((nx, ny))

def identify_regions(array):
    visited = set()
    regions = []
    
    rows, cols = array.shape
    for x in range(rows):
        for y in range(cols):
            if (x, y) not in visited:
                region = []
                flood_fill(array, x, y, visited, region)
                regions.append(region)
    
    return regions

def calculate_perimeter(region, array):
    perimeter = 0
    rows, cols = array.shape
    for x, y in region:
        for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if nx < 0 or nx >= rows or ny < 0 or ny >= cols or (nx, ny) not in region:
                perimeter += 1
    return perimeter

def calculate_sides(region, array):
    rows, cols = array.shape
    perimeters = []
    for x, y in region:
        for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if nx < 0 or nx >= rows or ny < 0 or ny >= cols or (nx, ny) not in region:
                perimeters.append((nx, ny))

    def flood_fill(start):
        stack = [(start, None)]  # (coordinate, direction)
        group = []
        while stack:
            (x, y), direction = stack.pop()
            group.append((x, y))
            for (nx, ny), new_direction in [((x-1, y), 'vertical'), ((x+1, y), 'vertical'), ((x, y-1), 'horizontal'), ((x, y+1), 'horizontal')]:
                if (nx, ny) in perimeters:
                    # Check if the adjacent coordinates are in a straight line
                    if direction is None or direction == new_direction:
                        stack.append(((nx, ny), new_direction))
        return group

    grouped_sides = []
    while len(perimeters) > 0:
        perimeter = perimeters.pop(0)
        group = flood_fill(perimeter)
        for coordinate in group:
            if coordinate in perimeters:
                perimeters.remove(coordinate)
        grouped_sides.append(group)

    adjacent_sides = 0
    for group in grouped_sides:
        adjacent_sides += len(group) - 1

    return calculate_perimeter(region, array) - adjacent_sides

def part1(contents):
    garden = convert_to_2d_array(contents)
    regions = identify_regions(garden)
    total_price = 0
    for region in regions:
        perimeter = calculate_perimeter(region, garden)
        price = len(region) * perimeter
        total_price += price
    return total_price

def part2(contents):
    garden = convert_to_2d_array(contents)
    regions = identify_regions(garden)
    total_price = 0
    for region in regions:
        print(f"{garden[region[0]]}", end= " = ")
        sides = calculate_sides(region, garden)
        price = len(region) * sides
        print(f"{len(region)} * {sides} = {price}")
        total_price += price
    print()
    return total_price

if __name__ == "__main__":
    test_input = load_input("day12_test").read()
    test_solution = part1(test_input)
    assert test_solution == 140, test_solution
    test_solution = part2(test_input)
    assert test_solution == 80, test_solution
    
    test_input = load_input("day12_test2").read()
    test_solution = part1(test_input)
    assert test_solution == 772, test_solution
    test_solution = part2(test_input)
    assert test_solution == 436, test_solution

    test_input = load_input("day12_test3").read()
    test_solution = part1(test_input)
    assert test_solution == 1930, test_solution
    test_solution = part2(test_input)
    assert test_solution == 1206, test_solution

    test_input = load_input("day12_test4").read()
    test_solution = part2(test_input)
    assert test_solution == 236, test_solution

    test_input = load_input("day12_test5").read()
    test_solution = part2(test_input)
    assert test_solution == 368, test_solution

    puzzle_input = load_input("day12").read()
    puzzle_solution = part1(puzzle_input)
    print(f"Part1: {puzzle_solution}")
    puzzle_solution = part2(puzzle_input)
    print(f"Part2: {puzzle_solution}")
