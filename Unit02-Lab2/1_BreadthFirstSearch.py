import time
from collections import deque

def breadth_first_search(graph, start, goal):
    """Finds the shortest path (by edges) in a graph using BFS."""
    start_time = time.time()
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        current_node, path = queue.popleft()

        if current_node == goal:
            exec_time = (time.time() - start_time) * 1000
            return path, exec_time

        if current_node not in visited:
            visited.add(current_node)
            for neighbor in graph.get(current_node, []):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    return None, 0


if __name__ == "__main__":
    # Sample Route Planning Graph
    city_map = {
        'Indore': ['Ujjain', 'Dewas', 'Mhow'],
        'Ujjain': ['Ratlam', 'Agar'],
        'Dewas': ['Bhopal', 'Shajapur'],
        'Mhow': ['Maheshwar'],
        'Ratlam': [],
        'Agar': [],
        'Bhopal': [],
        'Shajapur': [],
        'Maheshwar': []
    }

    start_city = 'Indore'
    goal_city = 'Bhopal'
    route, elapsed = breadth_first_search(city_map, start_city, goal_city)

    print(f"=== Breadth-First Search (BFS) Route Planner ===")
    print(f"Start: {start_city} -> Goal: {goal_city}")
    print(f"Shortest Route: {' -> '.join(route)}")
    print(f"Total Stops: {len(route) - 1} | Execution Time: {elapsed:.4f} ms")
