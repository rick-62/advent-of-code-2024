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
    perimeter_coords = set()
    
    for x, y in region:
        for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if nx < 0 or nx >= rows or ny < 0 or ny >= cols or (nx, ny) not in region:
                perimeter_coords.add((x, y))
    
    sides = 0
    visited = set()
    
    def dfs(x, y, dx, dy):
        while (x, y) in perimeter_coords:
            visited.add((x, y))
            x += dx
            y += dy
    
    for x, y in perimeter_coords:
        if (x, y) not in visited:
            sides += 1
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(x, y, dx, dy)
    
    return sides

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
#     garden = convert_to_2d_array(contents)
#     regions = identify_regions(garden)
#     total_price = 0
#     for region in regions:
#         sides = calculate_sides(region, garden)
#         price = len(region) * sides
#         total_price += price
#     return total_price
    pass

if __name__ == "__main__":
    test_input = load_input("day12_test").read()
    test_solution = part1(test_input)
    assert test_solution == 140, test_solution
    test_solution = part2(test_input)
    # assert test_solution == 80, test_solution
    
    test_input = load_input("day12_test2").read()
    test_solution = part1(test_input)
    assert test_solution == 772, test_solution
    test_solution = part2(test_input)
    # assert test_solution == 436, test_solution

    test_input = load_input("day12_test3").read()
    test_solution = part1(test_input)
    assert test_solution == 1930, test_solution
    test_solution = part2(test_input)
    # assert test_solution == 1206, test_solution


    puzzle_input = load_input("day12").read()
    puzzle_solution = part1(puzzle_input)
    print(f"Part1: {puzzle_solution}")
    puzzle_solution = part2(puzzle_input)
    print(f"Part2: {puzzle_solution}")
