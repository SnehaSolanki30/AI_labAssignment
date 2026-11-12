import time

# ==========================================================
# PROBLEM STATEMENT:
# Implement Depth-First Search (DFS) to traverse a graph 
# and find a path from a start city to a destination city.
# ==========================================================

def depth_first_search(graph, start, goal):
    """Finds a path from start to goal using Depth-First Search (LIFO Stack)."""
    start_time = time.time()
    visited = set()
    stack = [(start, [start])]

    while stack:
        current_node, path = stack.pop()

        if current_node == goal:
            exec_time = (time.time() - start_time) * 1000
            return path, exec_time

        if current_node not in visited:
            visited.add(current_node)
            # Add neighbors in reverse order so the first neighbor is explored first
            for neighbor in reversed(graph.get(current_node, [])):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

    return None, 0


if __name__ == "__main__":
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
    route, elapsed = depth_first_search(city_map, start_city, goal_city)

    print("=== Depth-First Search (DFS) Graph Traversal ===")
    print(f"Start: {start_city} -> Goal: {goal_city}")
    print(f"Path Found: {' -> '.join(route)}")
    print(f"Total Steps: {len(route) - 1} | Execution Time: {elapsed:.4f} ms")
