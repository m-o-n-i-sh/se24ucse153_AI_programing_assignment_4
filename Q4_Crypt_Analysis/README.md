# Cryptarithmetic Solver using CSP 
## Problem Statement

**Implement the crypt-analysis puzzle in Fig. 5.2a**

---

## Techniques Used
The solution uses **Brute Force with Constraint Checking**:
- **Permutation Generation** → tries all possible digit assignments
- **AllDiff Constraint** → ensures unique digits for letters
- **Leading Zero Constraint** → prevents invalid numbers
- **Arithmetic Validation** → checks equation correctness
---
## Algorithm Flow
1. Extract unique letters from the equation  
2. Generate all permutations of digits (0–9)  
3. Assign digits to letters  
4. Check constraints:
   - No repeated digits
   - No leading zeros  
5. Convert words into numbers  
6. Verify arithmetic condition  
7. Store valid solutions  
---
## Features
- Solve default puzzle: **TWO + TWO = FOUR**
- Accept **custom user-defined puzzles**
- Displays:
  - Letter → Digit mapping  
  - Arithmetic verification  
  - Search statistics  
---

## How to Run
```bash
python cryptarithm.py
```
---
## Sample Output
```
1. Use default (TWO + TWO = FOUR)
2. Enter your own puzzle

Solving: TWO + TWO = FOUR

Solution:
Letter → Digit Mapping:
F → 1
O → 4
R → 8
T → 7
U → 6
W → 3

Verification:
 734
+734
----
1468

Search Statistics:
Unique letters  : 6
Attempts tried  : 151200
Solutions found : 1
Execution Time  : 0.215643 seconds
```
