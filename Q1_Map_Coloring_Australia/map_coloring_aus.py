import time
VARIABLES = ["WA", "NT", "Q", "SA", "NSW", "V", "T"]
COLORS = ["Red", "Green", "Blue"]
DOMAINS = {var: list(COLORS) for var in VARIABLES}
NEIGHBORS = {
    "WA":  ["NT", "SA"],
    "NT":  ["WA", "SA", "Q"],
    "Q":   ["NT", "SA", "NSW"],
    "SA":  ["WA", "NT", "Q", "NSW", "V"],
    "NSW": ["Q", "SA", "V"],
    "V":   ["SA", "NSW"],
    "T":   []           
}
def is_consistent(variable: str, color: str, assignment: dict) -> bool:
    for neighbor in NEIGHBORS[variable]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True
def select_unassigned_variable(assignment: dict, domains: dict) -> str:
    unassigned = [v for v in VARIABLES if v not in assignment]
    return min(
    unassigned,key=lambda var: (len(domains[var]), -len(NEIGHBORS[var])))
def order_domain_values(variable: str, assignment: dict, domains: dict) -> list:
    def count_conflicts(color):
        return sum(
            1
            for neighbor in NEIGHBORS[variable]
            if neighbor not in assignment and color in domains[neighbor]
        )
    return sorted(domains[variable], key=count_conflicts)
def forward_check(variable: str, color: str, domains: dict) -> dict | None:
    new_domains = {v: list(d) for v, d in domains.items()}
    for neighbor in NEIGHBORS[variable]:
        if color in new_domains[neighbor]:
            new_domains[neighbor].remove(color)
            if not new_domains[neighbor]:
                return None
    return new_domains
def backtrack(assignment: dict, domains: dict, stats: dict) -> dict | None:
    if len(assignment) == len(VARIABLES):
        return assignment
    var = select_unassigned_variable(assignment, domains)
    for color in order_domain_values(var, assignment, domains):
        stats["nodes_explored"] += 1
        if is_consistent(var, color, assignment):
            assignment[var] = color
            stats["assignments"] += 1
            reduced_domains = forward_check(var, color, domains)
            if reduced_domains is not None:
                result = backtrack(assignment, reduced_domains, stats)
                if result is not None:
                    return result
            del assignment[var]
            stats["backtracks"] += 1
    return None
def solve_map_coloring():
    stats = {"nodes_explored": 0, "assignments": 0, "backtracks": 0}
    start = time.time()
    solution = backtrack({}, DOMAINS, stats)
    end = time.time()
    if solution:
        name_map = {
            "WA": "Western Australia",
            "NT": "Northern Territory",
            "Q":  "Queensland",
            "SA": "South Australia",
            "NSW":"New South Wales",
            "V":  "Victoria",
            "T":  "Tasmania",
        }
        print("\nSolution:\n")
        print(f"{'State/Territory':<20} {'Color'}")
        print(f"{'-'*20} {'-'*10}")
        for var in VARIABLES:
            print(f"{name_map[var]:<20} {solution[var]}")
        print("\nSearch Statistics:")
        print(f"Nodes explored : {stats['nodes_explored']}")
        print(f"Assignments    : {stats['assignments']}")
        print(f"Backtracks     : {stats['backtracks']}")
        total_constraints = sum(len(v) for v in NEIGHBORS.values())//2
        print(f"Total Constraints: {total_constraints}")
        print(f"Execution Time: {end - start:.6f} seconds")
    else:
        print("No solution found.")
if __name__ == "__main__":
    solve_map_coloring()