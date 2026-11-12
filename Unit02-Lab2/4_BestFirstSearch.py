import time
import heapq

# ==========================================================
# PROBLEM STATEMENT:
# Implement Greedy Best-First Search using a Priority Queue 
# to find a path from a start city to a goal city by always 
# expanding the node closest to the goal (lowest heuristic h(n)).
# ==========================================================

def best_first_search(graph, heuristics, start, goal):
    """Finds a path using Greedy Best-First Search (Priority Queue on h(n))."""
    start_time = time.time()
    visited = set()
    # Priority Queue stores tuples: (heuristic_value, current_node, path)
    pq = [(heuristics[start], start, [start])]

    while pq:
        h_val, current, path = heapq.heappop(pq)

        if current == goal:
            exec_time = (time.time() - start_time) * 1000
            return path, exec_time

        if current not in visited:
            visited.add(current)
            for neighbor in graph.get(current, []):
                if neighbor not in visited:
                    heapq.heappush(pq, (heuristics[neighbor], neighbor, path + [neighbor]))

    return None, 0


if __name__ == "__main__":
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

    # Heuristic values h(n): Estimated straight-line distance to Bhopal (in km)
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
    route, elapsed = best_first_search(city_graph, h_values, start_node, goal_node)

    print("=== Greedy Best-First Search ===")
    print(f"Start: {start_node} -> Goal: {goal_node}")
    print(f"Path Found: {' -> '.join(route)}")
    print(f"Total Steps: {len(route) - 1} | Execution Time: {elapsed:.4f} ms")
