from helper import load_input

def part1(contents):
    # Read all lines and split into columns
    lines = contents.readlines()
    list1 = []
    list2 = []

    for line in lines:
        numbers = list(map(int, line.split()))
        list1.append(numbers[0])
        list2.append(numbers[1])

    # Sort both lists
    list1.sort()
    list2.sort()

    # Subtract corresponding elements and sum the results
    result = sum(abs(a - b) for a, b in zip(list1, list2))

    return result

def part2(contents):
    # Read all lines and split into columns
    lines = contents.readlines()
    list1 = []
    list2 = []

    for line in lines:
        numbers = list(map(int, line.split()))
        list1.append(numbers[0])
        list2.append(numbers[1])

    # Calculate the frequency of each number in list2
    from collections import Counter
    list2_counter = Counter(list2)

    # Calculate the total similarity score
    similarity_score = sum(num * list2_counter[num] for num in list1)

    return similarity_score


if __name__ == "__main__":
    test_input = load_input('day01_test')
    test_solution = part1(test_input)
    assert test_solution == 11, test_solution

    puzzle_input = load_input('day01')
    puzzle_solution = part1(puzzle_input)
    print(puzzle_solution)

    test_input = load_input('day01_test')
    test_similarity_score = part2(test_input)
    assert test_similarity_score == 31, test_similarity_score

    puzzle_input = load_input('day01')
    puzzle_similarity_score = part2(puzzle_input)
    print(puzzle_similarity_score)