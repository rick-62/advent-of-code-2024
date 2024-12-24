import heapq

import numpy as np
from helper import load_input, print_map

def parse_input(text):
    lines = text.strip().split('\n')
    array = np.array([list(line) for line in lines])
    return array

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(array, start, finish):
    rows, cols = array.shape
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, finish)}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == finish:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        neighbors = [(current[0] + dx, current[1] + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]]
        neighbors = [(r, c) for r, c in neighbors if 0 <= r < rows and 0 <= c < cols]

        for neighbor in neighbors:
            if array[neighbor] == '#':
                continue

            tentative_g_score = g_score[current] + 1

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, finish)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None

def find_start_end(array):
    start = None
    end = None
    for r in range(array.shape[0]):
        for c in range(array.shape[1]):
            if array[r, c] == 'S':
                start = (r, c)
            elif array[r, c] == 'E':
                end = (r, c)
    return start, end

def find_hashtags_between_Os(puzzle_map):
    rows, cols = puzzle_map.shape
    hashtags_between_Os = []

    # Check horizontally
    for r in range(rows):
        for c in range(1, cols - 1):
            if puzzle_map[r, c] == '#' and puzzle_map[r, c - 1] == 'O' and puzzle_map[r, c + 1] == 'O':
                hashtags_between_Os.append((r, c))

    # Check vertically
    for c in range(cols):
        for r in range(1, rows - 1):
            if puzzle_map[r, c] == '#' and puzzle_map[r - 1, c] == 'O' and puzzle_map[r + 1, c] == 'O':
                hashtags_between_Os.append((r, c))

    return hashtags_between_Os

def part1(contents):
    puzzle_map = parse_input(contents)
    print_map(puzzle_map)
    start, end = find_start_end(puzzle_map)
    path = a_star_search(puzzle_map, start, end)
    for coord in path:
        puzzle_map[coord] = 'O'
        print_map(puzzle_map, wait=0.01)
    shortcuts = find_hashtags_between_Os(puzzle_map)
    for coord in shortcuts:
        puzzle_map[coord] = 'x'
        print_map(puzzle_map, wait=0.01)
    puzzle_map[puzzle_map == 'O'] = '.'
    print_map(puzzle_map, wait=0.01)
    puzzle_map[puzzle_map == 'x'] = '#'
    print_map(puzzle_map, wait=0.01)
    pass

def part2(contents):
    pass


if __name__ == "__main__":

    test_input = load_input("day20_test").read()
    test_solution = part1(test_input)
    assert test_solution == None, test_solution
    test_solution = part2(test_input)
    assert test_solution == None, test_solution

    puzzle_input = load_input("day20").read()
    puzzle_solution = part1(puzzle_input)
    print(f"Part1: {puzzle_solution}")
    puzzle_solution = part2(puzzle_input)
    print(f"Part2: {puzzle_solution}")
