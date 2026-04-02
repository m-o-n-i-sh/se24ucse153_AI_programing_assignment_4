# Sudoku Solver using CSP

## Problem Statement
**Implement the Sudoku puzzle using the CSP. (Refer 5.2.6)**

---
## Techniques Used
The solution uses **Constraint Propagation + Backtracking Search**:
- **AC-3 Algorithm** → enforces arc consistency
- **MRV (Minimum Remaining Values)** → selects most constrained variable
- **Forward Checking** → removes invalid values early
- **Backtracking Search** → explores valid assignments
- **Constraint Validation** → ensures Sudoku rules are followed
---
## Algorithm Flow
1. Convert puzzle into CSP (variables, domains, constraints)
2. Apply **AC-3** to reduce domains
3. Select unassigned variable (MRV)
4. Assign value and propagate constraints
5. Use **Backtracking** if needed
6. Repeat until solution is found
---
## Features
- Solve **default puzzle (textbook example)**
- Generate **random puzzles** with difficulty levels:
  - Easy
  - Medium
  - Hard
- Accept **custom user input**
- Displays **search statistics**
---
## How to Run
```bash
python sudoku_solver.py
```
---
## Sample Output
```
1. Solve default puzzle
2. Generate random puzzle
3. Enter your own puzzle

Default Puzzle(From textbook):
    3 |   2   | 6     
9     | 3   5 |     1 
    1 | 8   6 | 4     
---------------------
    8 | 1   2 | 9     
7     |       |     8 
    6 | 7   8 | 2     
---------------------
    2 | 6   9 | 5     
8     | 2   3 |     9 
    5 |   1   | 3     

Solution:
4 8 3 | 9 2 1 | 6 5 7 
9 6 7 | 3 4 5 | 8 2 1 
2 5 1 | 8 7 6 | 4 9 3 
---------------------
5 4 8 | 1 3 2 | 9 7 6 
7 2 9 | 5 6 4 | 1 3 8 
1 3 6 | 7 9 8 | 2 4 5 
---------------------
3 7 2 | 6 8 9 | 5 1 4 
8 1 4 | 2 5 3 | 7 6 9 
6 9 5 | 4 1 7 | 3 8 2 

Search Statistics:
Nodes explored : 0
Backtracks     : 0
AC-3 revisions : 392
Execution Time : 0.008264 seconds
Solved using AC-3 only
```
