from helper import load_input


def parse_input(content: str) -> tuple:
    dict_part, list_part = content.split("\n\n")
    
    # Parse the rules part
    dict_lines = dict_part.split("\n")
    rules = []
    for line in dict_lines:
        key, value = map(int, line.split("|"))
        rules.append((key, value))  # Append a tuple to the list
    
    # Parse the list of updates part
    list_lines = list_part.split("\n")
    updates = []
    for line in list_lines:
        updates.append(list(map(int, line.split(","))))
    
    return rules, updates


def is_update_valid(update: list, rules: list) -> bool:
    for rule in rules:
        key, value = rule
        try:
            if update.index(key) > update.index(value):
                return False
        except ValueError:
            continue
    return True

            
def get_middle_value_from_list(pages: list) -> int:
    middle_index = len(pages) // 2
    return pages[middle_index]

assert get_middle_value_from_list([1, 2, 3, 4, 5]) == 3


def part1(content: str) -> int:
    rules, updates = parse_input(content)

    total = 0
    for update in updates:
        if is_update_valid(update, rules):
            total += get_middle_value_from_list(update)
    
    return total
            
                              

def part2(content: str) -> int:
    pass

if __name__ == "__main__":
    test_input = load_input("day05_test").read() 
    test_solution = part1(test_input)
    assert test_solution == 143, test_solution

    puzzle_input = load_input("day05").read()



    print("Part 1:", part1(puzzle_input))
    print("Part 2:", "Not implemented")