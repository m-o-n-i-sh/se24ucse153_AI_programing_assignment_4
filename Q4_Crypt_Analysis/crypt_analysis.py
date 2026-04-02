import itertools
import time
def solve_cryptarithm(word1, word2, result):
    letters = sorted(set(word1 + word2 + result))
    print(f"\nSolving: {word1} + {word2} = {result}")
    if len(letters) > 10:
        print("Too many unique letters (max 10 allowed)")
        return
    digits = range(10)
    solutions = []
    attempts = 0
    start = time.time()
    for perm in itertools.permutations(digits, len(letters)):
        attempts += 1
        mapping = dict(zip(letters, perm))
        if (mapping[word1[0]] == 0 or 
            mapping[word2[0]] == 0 or 
            mapping[result[0]] == 0):
            continue
        n1 = int("".join(str(mapping[ch]) for ch in word1))
        n2 = int("".join(str(mapping[ch]) for ch in word2))
        res = int("".join(str(mapping[ch]) for ch in result))
        if n1 + n2 == res:
            solutions.append((mapping, n1, n2, res))
    end = time.time()
    print("\nSolution:")
    if not solutions:
        print("No solution found")
        print("\nSearch Statistics:")
        print(f"Unique letters  : {len(letters)}")
        print(f"Attempts tried  : {attempts}")
        print(f"Execution Time  : {end - start:.6f} seconds")
        return
    mapping, n1, n2, res = solutions[0]
    print("Letter → Digit Mapping:")
    for k in sorted(mapping):
        print(f"{k} → {mapping[k]}")
    width = max(len(str(n1)), len(str(n2)), len(str(res)))
    print("\nVerification:")
    print(f"{str(n1).rjust(width)}")
    print(f"+{str(n2).rjust(width-1)}")
    print("-" * width)
    print(f"{str(res).rjust(width)}")
    print("\nSearch Statistics:")
    print(f"Unique letters  : {len(letters)}")
    print(f"Attempts tried  : {attempts}")
    print(f"Solutions found : {len(solutions)}")
    print(f"Execution Time  : {end - start:.6f} seconds")
def main():
    print("1. Use default (TWO + TWO = FOUR)")
    print("2. Enter your own puzzle")
    choice = input("Enter choice: ")
    if choice == "1":
        word1, word2, result = "TWO", "TWO", "FOUR"
    elif choice == "2":
        print("\nEnter words (uppercase only):")
        word1 = input("First word  : ").strip().upper()
        word2 = input("Second word : ").strip().upper()
        result = input("Result word : ").strip().upper()
        if not (word1.isalpha() and word2.isalpha() and result.isalpha()):
            print("Invalid input (letters only)")
            return
    else:
        print("Invalid choice")
        return
    solve_cryptarithm(word1, word2, result)
if __name__ == "__main__":
    main()