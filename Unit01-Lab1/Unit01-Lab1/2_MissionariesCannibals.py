import time
from collections import deque

def missionaries_and_cannibals():
    """Solves Missionaries and Cannibals Problem using BFS."""
    start_time = time.time()
    initial_state = (3, 3, 1)  # (Missionaries_Left, Cannibals_Left, Boat_Pos)
    goal_state = (0, 0, 0)
    visited = set()
    queue = deque([(initial_state, [initial_state])])
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    def is_valid(m_left, c_left):
        m_right, c_right = 3 - m_left, 3 - c_left
        if not (0 <= m_left <= 3 and 0 <= c_left <= 3):
            return False
        if (m_left > 0 and c_left > m_left) or (m_right > 0 and c_right > m_right):
            return False
        return True

    while queue:
        (m, c, boat), path = queue.popleft()
        if (m, c, boat) == goal_state:
            return path, (time.time() - start_time) * 1000

        if (m, c, boat) in visited:
            continue
        visited.add((m, c, boat))

        for dm, dc in moves:
            new_state = (m - dm, c - dc, 0) if boat == 1 else (m + dm, c + dc, 1)
            if is_valid(new_state[0], new_state[1]) and new_state not in visited:
                queue.append((new_state, path + [new_state]))
    return None, 0

if __name__ == "__main__":
    path, elapsed = missionaries_and_cannibals()
    print(f"Missionaries & Cannibals Path ({len(path)-1} steps): {path}")
    print(f"Execution Time: {elapsed:.4f} ms")
