import numpy as np
from collections import deque
from helper import load_input

def convert_to_2d_array(contents):
    rows = contents.strip().split('\n')
    array = np.array([[np.uint8(char) for char in row] for row in rows], dtype=np.uint8)
    return array

def find_all_paths(array):
    rows, cols = array.shape
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    # Find all occurrences of 0
    starts = []
    for r in range(rows):
        for c in range(cols):
            if array[r, c] == 0:
                starts.append((r, c))

    all_paths = []

    for start in starts:
        queue = deque([(start, [start])])  # (current_position, path)
        visited = set()
        visited.add(start)

        while queue:
            (current_r, current_c), path = queue.popleft()

            if array[current_r, current_c] == 9:
                all_paths.append(path)
                continue  # Continue searching for other paths

            for dr, dc in directions:
                nr, nc = current_r + dr, current_c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    if array[nr, nc] == array[current_r, current_c] + 1:
                        queue.append(((nr, nc), path + [(nr, nc)]))
                        visited.add((nr, nc))

    return all_paths  # Return all paths found

def part1(contents):
    array = convert_to_2d_array(contents)
    paths = find_all_paths(array)
    return len(paths)

def part2(contents):
    array = convert_to_2d_array(contents)
    # Your logic for part2 here
    pass

if __name__ == "__main__":
    test_input = load_input("day10_test").read()
    test_solution = part1(test_input)
    assert test_solution == 36, test_solution
    test_solution = part2(test_input)
    assert test_solution == None, test_solution

    puzzle_input = load_input("day10").read()
    puzzle_solution = part1(puzzle_input)
    print(f"Part1: {puzzle_solution}")
    puzzle_solution = part2(puzzle_input)
    print(f"Part2: {puzzle_solution}")
