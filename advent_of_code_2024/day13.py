import re
from helper import load_input
import numpy as np

# solution incorrect & difficult to check as not test solution provided
# double check that finding the minimum cost as could be multiple solutins
# Try specialized algorithms for Diophantine equations


def parse_input(contents):
    pattern = re.compile(r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)")
    matches = pattern.findall(contents)
    result = [[(int(a), int(b)), (int(c), int(d)), (int(e), int(f))] for a, b, c, d, e, f in matches]
    return result

def calculate_final_position(A, B, config):
    (Ax, Ay), (Bx, By), _ = config
    X = A * Ax + B * Bx
    Y = A * Ay + B * By
    return X, Y


def part1(contents, costA=3, costB=1):
    data = parse_input(contents)

    total = 0
    for config in data:
        prize = config[2]
        for A in range(0, 100):
            for B in range(0, 100):
                X, Y = calculate_final_position(A, B, config)
                if X == prize[0] and Y == prize[1]:
                    total += A * costA + B * costB    

    return total


def solve_equations(A_coeff, B_coeff, prize):
    # Coefficients of the equations
    # A_coeff = (Ax, Ay)
    # B_coeff = (Bx, By)
    # prize = (Px, Py)
    
    # Construct the coefficient matrix and the constant vector
    A = np.array([[A_coeff[0], B_coeff[0]], [A_coeff[1], B_coeff[1]]])
    B = np.array([prize[0], prize[1]])
    
    # Solve the system of equations
    solution = np.linalg.solve(A, B)
    
    return solution

def part2(contents, costA=3, costB=1, offset=10000000000000):
    data = parse_input(contents)

    total = 0
    for config in data:
        prize = (config[2][0]+offset, config[2][1]+offset)
        solution = solve_equations(config[0], config[1], prize)
        final_position = calculate_final_position(int(solution[0]), int(solution[1]), config)
        if final_position == prize:
            total += int(solution[0]) * costA + int(solution[1]) * costB
    return total

if __name__ == "__main__":
    test_input = load_input("day13_test").read()
    test_solution = part1(test_input)
    assert test_solution == 480, test_solution
    test_solution = part2(test_input)
    # assert test_solution == None, test_solution

    puzzle_input = load_input("day13").read()
    puzzle_solution = part1(puzzle_input)
    print(f"Part1: {puzzle_solution}")
    puzzle_solution = part2(puzzle_input)
    print(f"Part2: {puzzle_solution}")
