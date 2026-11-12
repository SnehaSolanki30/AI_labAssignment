import time
from collections import deque

# ==========================================================
# PROBLEM STATEMENT:
# Implement an Autonomous Robot Navigation planner on a 2D 
# occupancy grid containing obstacles ('#') to compute a 
# collision-free shortest path from Start ('S') to Goal ('G').
# ==========================================================

def navigate_robot(grid, start, goal):
    """Finds the shortest collision-free path on a 2D grid using BFS."""
    start_time = time.time()
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start, [start])])
    visited = {start}
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    while queue:
        (r, c), path = queue.popleft()

        if (r, c) == goal:
            exec_time = (time.time() - start_time) * 1000
            return path, exec_time

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < rows
                and 0 <= nc < cols
                and grid[nr][nc] != '#'
                and (nr, nc) not in visited
            ):
                visited.add((nr, nc))
                queue.append(((nr, nc), path + [(nr, nc)]))

    return None, 0


if __name__ == "__main__":
    # 5x5 Warehouse Floor Map ('.' = Free Space, '#' = Obstacle)
    warehouse_map = [
        ['S', '.', '#', '.', '.'],
        ['.', '.', '#', '.', '#'],
        ['#', '.', '.', '.', '.'],
        ['.', '#', '#', '.', '#'],
        ['.', '.', '.', '.', 'G']
    ]

    start_pos = (0, 0)
    goal_pos = (4, 4)
    route, elapsed = navigate_robot(warehouse_map, start_pos, goal_pos)

    print("=== Robotics: Autonomous Obstacle-Free Path Planning ===")
    if route:
        # Mark path on grid for visual display
        display_grid = [row[:] for row in warehouse_map]
        for r, c in route[1:-1]:
            display_grid[r][c] = '*'

        for row in display_grid:
            print("  ", " ".join(row))

        print(f"\nCollision-Free Steps : {len(route) - 1}")
        print(f"Waypoints            : {route}")
        print(f"Execution Time       : {elapsed:.4f} ms")
    else:
        print("No collision-free path found.")
