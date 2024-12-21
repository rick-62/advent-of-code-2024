import numpy as np
from heapq import heappop, heappush
from helper import load_input, print_map

def parse_input(text):
    lines = text.strip().split('\n')
    array = np.array([list(line) for line in lines])
    return array

def calculate_turns(path):
    if len(path) < 2:
        return 0

    turns = 0
    current_direction = (0, 1)  # Starting direction is East

    for i in range(1, len(path)):
        prev = path[i - 1]
        curr = path[i]
        direction = (curr[0] - prev[0], curr[1] - prev[1])

        if direction != current_direction:
            turns += 1
            current_direction = direction

    return turns

def get_score(path):
    steps = len(path) - 1
    turns = calculate_turns(path)
    return steps + 1000 * turns

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def find_lowest_score_path(puzzle_map, start, end):
    def get_neighbors(position):
        x, y = position
        neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        valid_neighbors = [n for n in neighbors if 0 <= n[0] < puzzle_map.shape[0] and 0 <= n[1] < puzzle_map.shape[1] and puzzle_map[n] != '#']
        return valid_neighbors

    open_set = []
    heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}

    while open_set:
        _, current = heappop(open_set)

        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor in get_neighbors(current):
            tentative_g_score = g_score[current] + 1

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                heappush(open_set, (f_score[neighbor], neighbor))

    return []

def part1(contents):
    puzzle_map = parse_input(contents)
    start = tuple(np.argwhere(puzzle_map == 'S')[0])
    end = tuple(np.argwhere(puzzle_map == 'E')[0])
    best_path = find_lowest_score_path(puzzle_map, start, end)
    best_score = get_score(best_path)
    return best_score

def part2(contents):
    pass

if __name__ == "__main__":
    test_input = load_input("day16_test").read()
    test_solution = part1(test_input)
    assert test_solution == 7036, test_solution
    test_solution = part2(test_input)
    assert test_solution == None, test_solution

    test_input = load_input("day16_test2").read()
    test_solution = part1(test_input)
    assert test_solution == 11048, test_solution
    test_solution = part2(test_input)
    assert test_solution == None, test_solution

    puzzle_input = load_input("day16").read()
    puzzle_solution = part1(puzzle_input)
    print(f"Part1: {puzzle_solution}")
    puzzle_solution = part2(puzzle_input)
    print(f"Part2: {puzzle_solution}")
