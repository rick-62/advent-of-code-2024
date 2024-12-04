from helper import load_input
import numpy as np

def part1(contents):
    grid = [list(line) for line in contents.splitlines()]
    rows, cols = len(grid), len(grid[0])
    word = "XMAS"
    word_len = len(word)
    count = 0

    def search_direction(r, c, dr, dc):
        for i in range(word_len):
            nr, nc = r + dr * i, c + dc * i
            if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] != word[i]:
                return 0
        return 1

    directions = [
        (0, 1),  # right
        (0, -1),  # left
        (1, 0),  # down
        (-1, 0),  # up
        (1, 1),  # down-right
        (-1, -1),  # up-left
        (1, -1),  # down-left
        (-1, 1)  # up-right
    ]

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                count += search_direction(r, c, dr, dc)

    return count


def part2(contents):
    grid = np.array([list(line) for line in contents.splitlines()])
    rows, cols = grid.shape
    count = 0

    patterns = [
        np.array([['M', '.', 'S'],
                  ['.', 'A', '.'],
                  ['M', '.', 'S']]),
        np.array([['S', '.', 'M'],
                  ['.', 'A', '.'],
                  ['S', '.', 'M']]),
        np.array([['M', '.', 'M'],
                  ['.', 'A', '.'],
                  ['S', '.', 'S']]),
        np.array([['S', '.', 'S'],
                  ['.', 'A', '.'],
                  ['M', '.', 'M']])
    ]

    def matches_pattern(window, pattern):
        for i in range(3):
            for j in range(3):
                if pattern[i, j] != '.' and window[i, j] != pattern[i, j]:
                    return False
        return True

    for r in range(rows - 2):
        for c in range(cols - 2):
            window = grid[r:r+3, c:c+3]
            for pattern in patterns:
                if matches_pattern(window, pattern):
                    count += 1

    return count

if __name__ == "__main__":
    test_input = load_input('day04_test').read()
    test_solution = part1(test_input)
    assert test_solution == 18, test_solution
    test_solution = part2(test_input)
    assert test_solution == 9, test_solution

    puzzle_input = load_input('day04').read()
    puzzle_solution = part1(puzzle_input)
    print(puzzle_solution)
    print("Part 2:", part2(puzzle_input))