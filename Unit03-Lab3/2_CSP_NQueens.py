import time

# ==========================================================
# PROBLEM STATEMENT:
# Solve the N-Queens Constraint Satisfaction Problem (CSP) 
# using Backtracking so that N queens are placed on an N x N 
# chessboard with no two queens attacking each other 
# (same row, column, or diagonal).
# ==========================================================

def is_safe(board, row, col, n):
    """Checks if placing a queen at (row, col) violates any row or diagonal constraints."""
    # Check same row on the left side
    for c in range(col):
        if board[row][c] == 1:
            return False

    # Check upper-left diagonal
    for r, c in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[r][c] == 1:
            return False

    # Check lower-left diagonal
    for r, c in zip(range(row, n), range(col, -1, -1)):
        if board[r][c] == 1:
            return False

    return True


def solve_n_queens_util(board, col, n):
    """Recursive Backtracking solver for N-Queens CSP."""
    if col >= n:
        return True

    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1  # Assign value (Place Queen)
            if solve_n_queens_util(board, col + 1, n):
                return True
            board[row][col] = 0  # Backtrack

    return False


def solve_n_queens(n=4):
    start_time = time.time()
    board = [[0] * n for _ in range(n)]
    solved = solve_n_queens_util(board, 0, n)
    exec_time = (time.time() - start_time) * 1000
    return solved, board, exec_time


if __name__ == "__main__":
    N = 4
    success, solution_board, elapsed = solve_n_queens(N)

    print(f"=== Constraint Satisfaction Problem (CSP): {N}-Queens ===")
    if success:
        for row in solution_board:
            print("  ", " ".join("Q" if cell == 1 else "." for cell in row))
        print(f"\nSolution Found in {elapsed:.4f} ms")
    else:
        print("No solution exists.")
