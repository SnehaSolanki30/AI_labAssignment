import time
import heapq
from collections import deque

# Sample Weighted Graph and Heuristic values (to Goal 'G')
GRAPH = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 3), ('E', 5)],
    'C': [('F', 2)],
    'D': [('G', 4)],
    'E': [('G', 1)],
    'F': [('G', 3)],
    'G': []
}

HEURISTIC = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 3,
    'E': 1,
    'F': 2,
    'G': 0
}


# ==========================================
# 1. BREADTH-FIRST SEARCH (BFS)
# ==========================================
def bfs(graph, start, goal):
    start_time = time.time()
    visited = set()
    queue = deque([(start, [start], 0)])

    while queue:
        node, path, cost = queue.popleft()
        if node == goal:
            return path, cost, (time.time() - start_time) * 1000

        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor], cost + weight))

    return None, 0, 0


# ==========================================
# 2. DEPTH-FIRST SEARCH (DFS)
# ==========================================
def dfs(graph, start, goal):
    start_time = time.time()
    visited = set()
    stack = [(start, [start], 0)]

    while stack:
        node, path, cost = stack.pop()
        if node == goal:
            return path, cost, (time.time() - start_time) * 1000

        if node not in visited:
            visited.add(node)
            for neighbor, weight in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor], cost + weight))

    return None, 0, 0


# ==========================================
# 3. HILL CLIMBING SEARCH
# ==========================================
def hill_climbing(graph, heuristic, start, goal):
    start_time = time.time()
    current = start
    path = [current]
    total_cost = 0

    while current != goal:
        neighbors = graph[current]
        if not neighbors:
            break

        # Choose neighbor with lowest heuristic value
        best_neighbor, weight = min(neighbors, key=lambda x: heuristic[x[0]])
        if heuristic[best_neighbor] >= heuristic[current]:
            break  # Local optimum reached

        current = best_neighbor
        path.append(current)
        total_cost += weight

    elapsed = (time.time() - start_time) * 1000
    return (path if current == goal else None), total_cost, elapsed


# ==========================================
# 4. BEST-FIRST SEARCH (Greedy)
# ==========================================
def best_first_search(graph, heuristic, start, goal):
    start_time = time.time()
    visited = set()
    pq = [(heuristic[start], start, [start], 0)]

    while pq:
        _, node, path, cost = heapq.heappop(pq)
        if node == goal:
            return path, cost, (time.time() - start_time) * 1000

        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(pq, (heuristic[neighbor], neighbor, path + [neighbor], cost + weight))

    return None, 0, 0


# ==========================================
# 5. A* SEARCH ALGORITHM
# ==========================================
def a_star_search(graph, heuristic, start, goal):
    start_time = time.time()
    visited = set()
    # Priority Queue stores: (f_cost = g_cost + h_cost, g_cost, node, path)
    pq = [(heuristic[start], 0, start, [start])]

    while pq:
        f_cost, g_cost, node, path = heapq.heappop(pq)
        if node == goal:
            return path, g_cost, (time.time() - start_time) * 1000

        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    new_g = g_cost + weight
                    new_f = new_g + heuristic[neighbor]
                    heapq.heappush(pq, (new_f, new_g, neighbor, path + [neighbor]))

    return None, 0, 0


# ==========================================
# MAIN EXECUTION & COMPARISON
# ==========================================
if __name__ == "__main__":
    start_node, goal_node = 'A', 'G'
    algorithms = [
        ("Breadth-First Search (BFS)", bfs(GRAPH, start_node, goal_node)),
        ("Depth-First Search (DFS)", dfs(GRAPH, start_node, goal_node)),
        ("Hill Climbing", hill_climbing(GRAPH, HEURISTIC, start_node, goal_node)),
        ("Best-First Search", best_first_search(GRAPH, HEURISTIC, start_node, goal_node)),
        ("A* Search", a_star_search(GRAPH, HEURISTIC, start_node, goal_node))
    ]

    print(f"=== Search Algorithms Comparison ({start_node} -> {goal_node}) ===\n")
    for name, (path, cost, exec_time) in algorithms:
        print(f"{name}:")
        print(f"  Path: {path} | Path Cost: {cost} | Execution Time: {exec_time:.4f} ms\n")
