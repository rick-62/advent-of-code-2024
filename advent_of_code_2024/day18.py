import heapq
from helper import load_input, print_map
import numpy as np

def parse_input(input_str):
    lines = input_str.strip().split('\n')
    return [tuple(map(int, line.split(','))) for line in lines]

def create_array(start, finish):
    rows = finish[0] - start[0] + 1
    cols = finish[1] - start[1] + 1
    return np.full((rows, cols), '.', dtype=str)

def add_hash_to_array(array, coord):
    array[coord] = '#'

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

def part1(contents, start=(0,0), finish=(70,70), bytes=1024):
    data = parse_input(contents)
    array = create_array(start, finish)
    print_map(array)
    for i in range(bytes):
        add_hash_to_array(array, data[i])
    shortest_path = a_star_search(array, start, finish)
    for coord in shortest_path:
        array[coord] = 'O'
        print_map(array, wait=0.01)
    return len(shortest_path) - 1

def part2(contents, start=(0,0), finish=(70,70)):
    data = parse_input(contents)
    array = create_array(start, finish)
    for coord in data:
        add_hash_to_array(array, coord)
        shortest_path = a_star_search(array, start, finish)
        if shortest_path == None:
            return ','.join(str(x) for x in coord)
    pass

if __name__ == "__main__":
    test_input = load_input("day18_test").read()
    test_solution = part1(test_input, finish=(6,6), bytes=12)
    assert test_solution == 22, test_solution
    test_solution = part2(test_input, finish=(6,6))
    assert test_solution == "6,1", test_solution

    puzzle_input = load_input("day18").read()
    puzzle_solution = part1(puzzle_input, bytes=1024)
    print(f"Part1: {puzzle_solution}")
    puzzle_solution = part2(puzzle_input)
    print(f"Part2: {puzzle_solution}")
