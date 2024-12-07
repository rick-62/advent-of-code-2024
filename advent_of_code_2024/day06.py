import numpy as np
from helper import load_input

def parse_contents(content):
    lines = content.strip().split('\n')
    return np.array([list(line) for line in lines])

class GameBoard:
    def __init__(self, content):
        self.board = parse_contents(content)
        self.directions = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}
        self.guard_position = None
        self.guard_direction = None
        self.find_guard()

    def find_guard(self):
        for i, row in enumerate(self.board):
            for j, cell in enumerate(row):
                if cell in self.directions:
                    self.guard_position = (i, j)
                    self.guard_direction = cell
                    return

    def move_guard(self):
        visited = set()
        while True:
            x, y = self.guard_position
            dx, dy = self.directions[self.guard_direction]
            new_x, new_y = x + dx, y + dy

            if not (0 <= new_x < self.board.shape[0] and 0 <= new_y < self.board.shape[1]):
                self.board[x, y] = 'X'  # Mark the last position before falling off
                break  # Guard falls off the gameboard

            if self.board[new_x, new_y] == '#':
                self.rotate_guard()
            else:
                self.board[x, y] = 'X'
                self.guard_position = (new_x, new_y)

            state = (self.guard_position, self.guard_direction)
            if state in visited:
                break  # Guard is stuck in a loop
            visited.add(state)

    def rotate_guard(self):
        rotations = {'<': '^', '^': '>', '>': 'v', 'v': '<'}
        self.guard_direction = rotations[self.guard_direction]

    def count_Xs(self):
        return np.sum(self.board == 'X')

    def __str__(self):
        return '\n'.join(''.join(row) for row in self.board)

    def simulate_with_obstruction(self, obstruction_position):
        original_board = self.board.copy()
        original_guard_position = self.guard_position
        original_guard_direction = self.guard_direction

        if obstruction_position == self.guard_position:
            return False

        self.board[obstruction_position] = '#'
        self.guard_position = None
        self.guard_direction = None
        self.find_guard()
        visited = set()
        stuck = False
        while True:
            x, y = self.guard_position
            dx, dy = self.directions[self.guard_direction]
            new_x, new_y = x + dx, y + dy

            if not (0 <= new_x < self.board.shape[0] and 0 <= new_y < self.board.shape[1]):
                break  # Guard falls off the gameboard

            if self.board[new_x, new_y] == '#':
                self.rotate_guard()
            else:
                self.guard_position = (new_x, new_y)

            state = (self.guard_position, self.guard_direction)
            if state in visited:
                stuck = True  # Guard is stuck in a loop
                break
            visited.add(state)

        self.board = original_board
        self.guard_position = original_guard_position
        self.guard_direction = original_guard_direction

        return stuck

def part1(content):
    gameboard = GameBoard(content)
    gameboard.move_guard()
    return gameboard.count_Xs()

def part2(content):
    gameboard = GameBoard(content)
    gameboard.move_guard()
    # print(gameboard)
    possible_positions = np.argwhere(gameboard.board == 'X')

    gameboard = GameBoard(content)

    count = 0
    for pos in possible_positions:
        if gameboard.simulate_with_obstruction(tuple(pos)):
            count += 1
    return count

if __name__ == "__main__":
    test_input = load_input("day06_test").read()
    test_solution = part1(test_input)
    assert test_solution == 41, test_solution
    test_solution = part2(test_input)
    assert test_solution == 6, test_solution

    puzzle_input = load_input("day06").read()
    print(part1(puzzle_input))
    print(part2(puzzle_input))