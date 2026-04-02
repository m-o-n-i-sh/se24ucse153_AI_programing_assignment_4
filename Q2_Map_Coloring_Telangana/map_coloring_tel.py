import time
DISTRICTS = {
    "ADB": "Adilabad",
    "KBA": "Kumurambheem Asifabad",
    "MAN": "Mancherial",
    "NIR": "Nirmal",
    "NZB": "Nizamabad",
    "JAG": "Jagtial",
    "PED": "Peddapalli",
    "JSB": "Jayashankar Bhupalpally",
    "RSI": "Rajanna Sircilla",
    "KRM": "Karimnagar",
    "KMR": "Kamareddy",
    "MDK": "Medak",
    "SNG": "Sangareddy",
    "SID": "Siddipet",
    "JNG": "Jangaon",
    "YDB": "Yadadri Bhuvanagiri",
    "MLG": "Mulugu",
    "BKG": "Bhadradri Kothagudem",
    "KHM": "Khammam",
    "SUR": "Suryapet",
    "NLG": "Nalgonda",
    "MHB": "Mahabubabad",
    "WGU": "Warangal Urban",
    "WGR": "Warangal Rural",
    "HYD": "Hyderabad",
    "MMG": "Medchal Malkajgiri",
    "RNG": "Rangareddy",
    "VKB": "Vikarabad",
    "MBN": "Mahabubnagar",
    "NGK": "Nagarkurnool",
    "WNP": "Wanaparthy",
    "JLG": "Jogulamba Gadwal",
    "NRY": "Narayanpet",
}
NEIGHBORS = {
    "ADB": ["NIR", "KBA", "NZB"],
    "KBA": ["ADB", "MAN", "NIR"],
    "MAN": ["KBA", "NIR", "JAG", "PED"],
    "NIR": ["ADB", "KBA", "MAN", "NZB", "KMR", "JAG"],
    "NZB": ["ADB", "NIR", "KMR"],
    "JAG": ["NIR", "MAN", "PED", "RSI", "KRM"],
    "PED": ["MAN", "JAG", "KRM", "JSB"],
    "JSB": ["PED", "KRM", "MLG", "WGU", "WGR"],
    "RSI": ["JAG", "KRM", "SID", "KMR"],
    "KRM": ["JAG", "PED", "RSI", "SID", "JNG", "JSB"],
    "KMR": ["NZB", "NIR", "RSI", "MDK", "SID"],
    "MDK": ["KMR", "SNG", "SID", "MMG"],
    "SNG": ["MDK", "VKB", "HYD", "MMG"],
    "SID": ["KMR", "RSI", "KRM", "MDK", "JNG", "YDB", "MMG"],
    "JNG": ["KRM", "SID", "WGU", "WGR", "YDB", "MHB"],
    "YDB": ["SID", "JNG", "NLG", "SUR", "MHB", "MMG"],
    "MLG": ["JSB", "WGU", "MHB", "BKG"],
    "BKG": ["MLG", "MHB", "KHM"],
    "KHM": ["BKG", "MHB", "SUR"],
    "SUR": ["YDB", "MHB", "KHM", "NLG"],
    "NLG": ["YDB", "SUR", "RNG", "MBN"],
    "MHB": ["JNG", "YDB", "MLG", "BKG", "KHM", "SUR", "WGU"],
    "WGU": ["JSB", "JNG", "MHB", "MLG", "WGR"],
    "WGR": ["JSB", "JNG", "WGU"],
    "HYD": ["MMG", "SNG", "RNG"],
    "MMG": ["MDK", "SID", "YDB", "HYD", "RNG"],
    "RNG": ["SNG", "MMG", "HYD", "NLG", "VKB", "MBN"],
    "VKB": ["SNG", "RNG", "MBN", "NRY"],
    "MBN": ["RNG", "VKB", "NRY", "NGK", "WNP", "NLG"],
    "NGK": ["MBN", "WNP", "JLG"],
    "WNP": ["MBN", "NGK", "JLG"],
    "JLG": ["WNP", "NGK", "NRY"],
    "NRY": ["VKB", "MBN", "JLG"],
}
VARIABLES = list(DISTRICTS.keys())
def get_colors():
    choice = input("Use default colors (R,G,B,Y)? (y/n): ").lower()

    if choice == 'y':
        return ["R", "G", "B", "Y"]
    else:
        user_colors = input("Enter colors (comma separated): ")
        colors = [c.strip() for c in user_colors.split(",")]

        if len(colors) < 3:
            print("Warning: Too few colors, solution may fail.")

        return colors
COLORS = get_colors()
DOMAINS = {v: list(COLORS) for v in VARIABLES}
def is_consistent(var, color, assignment):
    return all(assignment.get(nb) != color for nb in NEIGHBORS[var])
def mrv(assignment, domains):
    unassigned = [v for v in VARIABLES if v not in assignment]
    return min(unassigned, key=lambda v: len(domains[v]))
def lcv(var, assignment, domains):
    def conflicts(c):
        return sum(
            1 for nb in NEIGHBORS[var]
            if nb not in assignment and c in domains[nb]
        )
    return sorted(domains[var], key=conflicts)
def forward_check(var, color, domains):
    new = {v: list(d) for v, d in domains.items()}
    for nb in NEIGHBORS[var]:
        if color in new[nb]:
            new[nb].remove(color)
            if not new[nb]:
                return None
    return new
def backtrack(assign, domains, stats):
    if len(assign) == len(VARIABLES):
        return assign
    var = mrv(assign, domains)
    for color in lcv(var, assign, domains):
        stats["nodes"] += 1
        if is_consistent(var, color, assign):
            assign[var] = color
            stats["assignments"] += 1
            new_domains = forward_check(var, color, domains)
            if new_domains:
                result = backtrack(assign, new_domains, stats)
                if result:
                    return result
            del assign[var]
            stats["backtracks"] += 1
    return None
def solve():
    stats = {"nodes": 0, "assignments": 0, "backtracks": 0}
    start = time.time()
    solution = backtrack({}, DOMAINS, stats)
    end = time.time()
    total_constraints = sum(len(v) for v in NEIGHBORS.values()) // 2
    if not solution:
        print("\nNo solution found with given colors.")
        return
    print("Solution:\n")
    print(f"{'District':<30} {'Color'}")
    print(f"{'-'*30} {'-'*10}")
    for code in VARIABLES:
        print(f"{DISTRICTS[code]:<30} {solution[code]}")
    print("\nSearch Statistics:")
    print(f"Nodes explored : {stats['nodes']}")
    print(f"Assignments    : {stats['assignments']}")
    print(f"Backtracks     : {stats['backtracks']}")
    print(f"Total Constraints: {total_constraints}")
    print(f"Execution Time: {end - start:.6f} seconds")
if __name__ == "__main__":
    solve()