# Map Coloring using CSP (Australia)
##  Problem Statement
**Implement the Map Coloring problem using CSP for the seven principal states and territories of Australia namely: WA, NT, Queensland, SA, NSW, V, T.**

---
## Techniques Used
The solution uses **Backtracking Search with heuristics**:
- **MRV (Minimum Remaining Values)** → selects variable with least domain
- **Degree Heuristic** → prioritizes most constrained variable
- **LCV (Least Constraining Value)** → chooses least restrictive color
- **Forward Checking** → reduces domain of neighbors
- **Constraint Checking** → ensures valid assignments
---
## Algorithm Flow
1. Select an unassigned variable (MRV + Degree heuristic)
2. Order domain values (LCV)
3. Check consistency with constraints
4. Apply forward checking
5. Recursively assign values (Backtracking)
6. If failure → backtrack
---
## How to Run
```bash
python map_coloring_aus.py
```
---
## Sample Output
```
Solution:

State/Territory      Color
-------------------- ----------
Western Australia    Red
Northern Territory   Green
Queensland           Red
South Australia      Blue
New South Wales      Green
Victoria             Red
Tasmania             Blue

Search Statistics:
Nodes explored : 7
Assignments    : 7
Backtracks     : 0
Total Constraints: 18
Execution Time: 0.000049 seconds
```



