import time
import heapq

# ==========================================================
# PROBLEM STATEMENT:
# Implement the A* (A-Star) Search algorithm to find the 
# optimal shortest path from a start city to a goal city 
# using f(n) = g(n) + h(n), where g(n) is the actual path 
# cost and h(n) is the heuristic estimate to the goal.
# ==========================================================

def a_star_search(graph, heuristics, start, goal):
    """Finds the optimal shortest path using A* Search: f(n) = g(n) + h(n)."""
    start_time = time.time()
    # Priority Queue stores: (f_cost, g_cost, current_node, path)
    pq = [(heuristics[start], 0, start, [start])]
    visited_costs = {start: 0}

    while pq:
        f_cost, g_cost, current, path = heapq.heappop(pq)

        if current == goal:
            exec_time = (time.time() - start_time) * 1000
            return path, g_cost, exec_time

        for neighbor, step_cost in graph.get(current, []):
            new_g = g_cost + step_cost
            if neighbor not in visited_costs or new_g < visited_costs[neighbor]:
                visited_costs[neighbor] = new_g
                new_f = new_g + heuristics[neighbor]
                heapq.heappush(pq, (new_f, new_g, neighbor, path + [neighbor]))

    return None, float('inf'), 0


if __name__ == "__main__":
    # Weighted graph: 'City': [('Neighbor', actual_distance_in_km), ...]
    weighted_city_graph = {
        'Indore': [('Dewas', 40), ('Ujjain', 55), ('Mhow', 25)],
        'Dewas': [('Shajapur', 65), ('Bhopal', 155)],
        'Ujjain': [('Agar', 70)],
        'Mhow': [('Maheshwar', 75)],
        'Shajapur': [('Bhopal', 105)],
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
    route, total_distance, elapsed = a_star_search(
        weighted_city_graph, h_values, start_node, goal_node
    )

    print("=== A* (A-Star) Optimal Search ===")
    print(f"Start: {start_node} -> Goal: {goal_node}")
    print(f"Optimal Route: {' -> '.join(route)}")
    print(f"Total Distance: {total_distance} km | Execution Time: {elapsed:.4f} ms")
