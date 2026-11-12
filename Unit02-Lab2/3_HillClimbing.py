import time

# ==========================================================
# PROBLEM STATEMENT:
# Implement the Hill Climbing Heuristic Search algorithm to 
# reach a goal state by always moving to a neighboring state 
# with a better (lower) heuristic distance.
# ==========================================================

def hill_climbing(graph, heuristics, start, goal):
    """Finds a path using Steepest-Ascent / Greedy Hill Climbing."""
    start_time = time.time()
    current = start
    path = [current]

    while current != goal:
        neighbors = graph.get(current, [])
        if not neighbors:
            # Dead end reached
            return None, (time.time() - start_time) * 1000

        # Select the neighbor with the lowest heuristic value (closest to goal)
        best_neighbor = min(neighbors, key=lambda node: heuristics[node])

        # Stop if no neighbor improves the current heuristic (Local Optimum)
        if heuristics[best_neighbor] >= heuristics[current]:
            return None, (time.time() - start_time) * 1000

        current = best_neighbor
        path.append(current)

    exec_time = (time.time() - start_time) * 1000
    return path, exec_time


if __name__ == "__main__":
    # Graph representing connected locations
    city_graph = {
        'Indore': ['Dewas', 'Ujjain', 'Mhow'],
        'Dewas': ['Shajapur', 'Bhopal'],
        'Ujjain': ['Agar'],
        'Mhow': ['Maheshwar'],
        'Shajapur': ['Bhopal'],
        'Agar': [],
        'Maheshwar': [],
        'Bhopal': []
    }

    # Heuristic values (Estimated straight-line distance in km to Bhopal)
    h_values = {
        'Indore': 190,
        'Dewas': 150,
        'Ujjain': 185,
        'Mhow': 210,
        'Shajapur': 100,
        'Agar': 170,
        'Maheshwar': 240,
        'Bhopal': 0
    }

    start_node = 'Indore'
    goal_node = 'Bhopal'
    route, elapsed = hill_climbing(city_graph, h_values, start_node, goal_node)

    print("=== Hill Climbing Heuristic Search ===")
    print(f"Start: {start_node} -> Goal: {goal_node}")
    if route:
        print(f"Path Found: {' -> '.join(route)}")
        print(f"Total Steps: {len(route) - 1} | Execution Time: {elapsed:.4f} ms")
    else:
        print("Stuck at Local Optimum / Dead End! Goal not reached.")
