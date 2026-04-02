import copy
import time
import random
ROWS = 'ABCDEFGHI'
COLS = '123456789'
VARIABLES = [r + c for r in ROWS for c in COLS]
ROW_UNITS = [[r + c for c in COLS] for r in ROWS]
COL_UNITS = [[r + c for r in ROWS] for c in COLS]
BOX_UNITS = [
    [r + c for r in rs for c in cs]
    for rs in ('ABC', 'DEF', 'GHI')
    for cs in ('123', '456', '789')
]
ALL_UNITS = ROW_UNITS + COL_UNITS + BOX_UNITS
UNITS_FOR = {v: [u for u in ALL_UNITS if v in u] for v in VARIABLES}
PEERS = {v: set(vv for u in UNITS_FOR[v] for vv in u) - {v} for v in VARIABLES}
DEFAULT_PUZZLE = [
    [0, 0, 3, 0, 2, 0, 6, 0, 0],
    [9, 0, 0, 3, 0, 5, 0, 0, 1],
    [0, 0, 1, 8, 0, 6, 4, 0, 0],
    [0, 0, 8, 1, 0, 2, 9, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 0, 6, 7, 0, 8, 2, 0, 0],
    [0, 0, 2, 6, 0, 9, 5, 0, 0],
    [8, 0, 0, 2, 0, 3, 0, 0, 9],
    [0, 0, 5, 0, 1, 0, 3, 0, 0],
]
def print_puzzle(puzzle, title="Puzzle"):
    print(f"\n{title}:")
    for i, row in enumerate(puzzle):
        if i % 3 == 0 and i != 0:
            print("-" * 21)

        for j, val in enumerate(row):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")

            print(val if val != 0 else " ", end=" ")
        print()
def make_domains(puzzle):
    domains = {}
    for i, r in enumerate(ROWS):
        for j, c in enumerate(COLS):
            var = r + c
            val = puzzle[i][j]
            domains[var] = {val} if val != 0 else set(range(1, 10))
    return domains
def ac3(domains, stats):
    queue = [(xi, xj) for xi in VARIABLES for xj in PEERS[xi]]
    while queue:
        xi, xj = queue.pop(0)
        if revise(domains, xi, xj):
            stats["ac3_revisions"] += 1
            if not domains[xi]:
                return False
            for xk in PEERS[xi] - {xj}:
                queue.append((xk, xi))
    return True
def revise(domains, xi, xj):
    revised = False
    if len(domains[xj]) == 1:
        val = next(iter(domains[xj]))
        if val in domains[xi]:
            domains[xi].remove(val)
            revised = True
    return revised
def select_unassigned_variable(domains):
    unassigned = [v for v in VARIABLES if len(domains[v]) > 1]
    return min(unassigned, key=lambda v: len(domains[v])) if unassigned else None
def assign(var, val, domains):
    new = copy.deepcopy(domains)
    new[var] = {val}

    for peer in PEERS[var]:
        if val in new[peer]:
            new[peer].remove(val)
            if not new[peer]:
                return None
    return new
def backtrack(domains, stats):
    if all(len(d) == 1 for d in domains.values()):
        return domains
    var = select_unassigned_variable(domains)
    for val in domains[var]:
        stats["nodes"] += 1
        new_domains = assign(var, val, domains)
        if new_domains is None:
            stats["backtracks"] += 1
            continue
        if not ac3(new_domains, stats):
            stats["backtracks"] += 1
            continue
        result = backtrack(new_domains, stats)
        if result:
            return result
        stats["backtracks"] += 1
    return None
def solve(puzzle):
    stats = {"nodes": 0, "backtracks": 0, "ac3_revisions": 0}
    domains = make_domains(puzzle)
    start = time.time()
    if not ac3(domains, stats):
        print("\n Puzzle is invalid (AC-3 failed)")
        return
    result = backtrack(domains, stats)
    end = time.time()
    if result is None:
        print("\nNo solution exists for this puzzle")
        return
    solution = [
        [next(iter(result[r + c])) for c in COLS]
        for r in ROWS
    ]
    print_puzzle(solution, "Solution")
    print("\nSearch Statistics:")
    print(f"Nodes explored : {stats['nodes']}")
    print(f"Backtracks     : {stats['backtracks']}")
    print(f"AC-3 revisions : {stats['ac3_revisions']}")
    print(f"Execution Time : {end - start:.6f} seconds")
    if stats["nodes"] == 0:
        print("Solved using AC-3 only")
    else:
        print("Solved using AC-3 + Backtracking")
def generate_full_solution():
    empty = [[0]*9 for _ in range(9)]
    domains = make_domains(empty)
    stats = {"nodes": 0, "backtracks": 0, "ac3_revisions": 0}
    ac3(domains, stats)
    result = backtrack(domains, stats)
    return [
        [next(iter(result[r + c])) for c in COLS]
        for r in ROWS
    ]
def generate_puzzle(difficulty):
    board = generate_full_solution()
    if difficulty == "easy":
        remove = 30
    elif difficulty == "medium":
        remove = 40
    else:
        remove = 50
    for _ in range(remove):
        i = random.randint(0, 8)
        j = random.randint(0, 8)
        board[i][j] = 0
    return board
def input_puzzle():
    print("\nEnter Sudoku (row by row)")
    print("Use space or comma separated values (0 for empty)\n")
    puzzle = []
    for i in range(9):
        while True:
            try:
                row_input = input(f"Row {i+1}: ")
                row_input = row_input.replace(',', ' ')
                row = list(map(int, row_input.split()))
                if len(row) != 9:
                    raise ValueError("Row must have exactly 9 numbers")
                if any(num < 0 or num > 9 for num in row):
                    raise ValueError("Numbers must be between 0 and 9")
                puzzle.append(row)
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Try again.\n")
    return puzzle
def is_valid(puzzle):
    for i in range(9):
        row = [x for x in puzzle[i] if x != 0]
        if len(row) != len(set(row)):
            return Falsez
        col = [puzzle[r][i] for r in range(9) if puzzle[r][i] != 0]
        if len(col) != len(set(col)):
            return False
    for box_r in range(0, 9, 3):
        for box_c in range(0, 9, 3):
            nums = []
            for i in range(3):
                for j in range(3):
                    val = puzzle[box_r+i][box_c+j]
                    if val != 0:
                        nums.append(val)
            if len(nums) != len(set(nums)):
                return False
    return True
def main():
    print("1. Solve default puzzle")
    print("2. Generate random puzzle")
    print("3. Enter your own puzzle")
    choice = input("Enter choice: ")
    if choice == '1':
        puzzle = DEFAULT_PUZZLE
        print_puzzle(puzzle, "Default Puzzle(From textbook)")
    elif choice == '2':
        diff = input("Choose difficulty (easy/medium/hard): ").lower()
        if diff not in ["easy", "medium", "hard"]:
            print("Invalid difficulty, defaulting to medium")
            diff = "medium"
        puzzle = generate_puzzle(diff)
        print_puzzle(puzzle, f"Generated Puzzle ({diff})")
    elif choice == '3':
        puzzle = input_puzzle()
        print_puzzle(puzzle, "Your Input Puzzle")
    else:
        print("Invalid choice")
        return
    if not is_valid(puzzle):
        print("\nInvalid puzzle: violates Sudoku constraints")
        return
    solve(puzzle)
if __name__ == "__main__":
    main()