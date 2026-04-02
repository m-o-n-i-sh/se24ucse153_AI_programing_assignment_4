# Map Coloring using CSP (Telangana - 33 Districts)
##  Problem Statement
**Apply the Map coloring problem to the 33 districts of Telangana. A sample output of your code may look as shown. Choose your own colors.**

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
1. Select an unassigned variable (MRV heuristic)  
2. Order domain values (LCV)  
3. Check consistency with constraints  
4. Apply forward checking  
5. Recursively assign values (Backtracking)  
6. If failure → backtrack  
---
## How to Run
```bash
python map_coloring_tel.py
```
---
## Sample Output
```
Use default colors (R,G,B,Y)? (y/n): y

Solution:

District                       Color
------------------------------ ----------
Adilabad                       R
Kumurambheem Asifabad          G
Mancherial                     R
Nirmal                         B
Nizamabad                      G
...
Narayanpet                     G

Search Statistics:
Nodes explored : 35
Assignments    : 33
Backtracks     : 0
Total Constraints: 72
Execution Time: 0.000424 seconds
```
