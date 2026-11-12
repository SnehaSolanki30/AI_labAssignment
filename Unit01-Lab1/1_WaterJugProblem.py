import time
from collections import deque

def water_jug_solver(jug1_cap, jug2_cap, target):
    """Solves Water Jug Problem using Breadth-First Search (BFS)."""
    start_time = time.time()
    visited = set()
    queue = deque([((0, 0), [(0, 0)])])

    while queue:
        (j1, j2), path = queue.popleft()
        if j1 == target or j2 == target:
            return path, (time.time() - start_time) * 1000

        if (j1, j2) in visited:
            continue
        visited.add((j1, j2))

        next_states = [
            (jug1_cap, j2),  # Fill Jug 1
            (j1, jug2_cap),  # Fill Jug 2
            (0, j2),         # Empty Jug 1
            (j1, 0),         # Empty Jug 2
            (j1 - min(j1, jug2_cap - j2), j2 + min(j1, jug2_cap - j2)),  # Pour 1 -> 2
            (j1 + min(j2, jug1_cap - j1), j2 - min(j2, jug1_cap - j1))   # Pour 2 -> 1
        ]

        for state in next_states:
            if state not in visited:
                queue.append((state, path + [state]))
    return None, 0

if __name__ == "__main__":
    path, elapsed = water_jug_solver(4, 3, 2)
    print(f"Water Jug Solution Path ({len(path)-1} steps): {path}")
    print(f"Execution Time: {elapsed:.4f} ms")
