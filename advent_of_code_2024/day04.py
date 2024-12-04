from helper import load_input

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

if __name__ == "__main__":
    test_input = load_input('day04_test').read()
    test_solution = part1(test_input)
    assert test_solution == 18, test_solution

    puzzle_input = load_input('day04').read()
    puzzle_solution = part1(puzzle_input)
    print(puzzle_solution)