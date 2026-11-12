import time
import math

# ==========================================================
# PROBLEM STATEMENT:
# Implement the Minimax Algorithm with Alpha-Beta Pruning 
# to find the optimal move for an AI player ('X') against 
# an opponent ('O') in a game of Tic-Tac-Toe.
# ==========================================================

def evaluate_board(board):
    """Returns +10 if 'X' wins, -10 if 'O' wins, or 0 otherwise."""
    win_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    for a, b, c in win_combinations:
        if board[a] == board[b] == board[c] and board[a] != ' ':
            return 10 if board[a] == 'X' else -10
    return 0


def minimax_alpha_beta(board, depth, alpha, beta, is_maximizing):
    """Minimax search with Alpha-Beta pruning to evaluate game states."""
    score = evaluate_board(board)

    # Terminal states (Win, Loss, or Draw)
    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if ' ' not in board:
        return 0

    if is_maximizing:
        best_val = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                best_val = max(best_val, minimax_alpha_beta(board, depth + 1, alpha, beta, False))
                board[i] = ' '
                alpha = max(alpha, best_val)
                if beta <= alpha:
                    break  # Beta cut-off (Pruning)
        return best_val
    else:
        best_val = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                best_val = min(best_val, minimax_alpha_beta(board, depth + 1, alpha, beta, True))
                board[i] = ' '
                beta = min(beta, best_val)
                if beta <= alpha:
                    break  # Alpha cut-off (Pruning)
        return best_val


def find_best_move(board):
    """Finds the optimal next move index (0-8) for AI player 'X'."""
    start_time = time.time()
    best_val = -math.inf
    best_move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            move_val = minimax_alpha_beta(board, 0, -math.inf, math.inf, False)
            board[i] = ' '
            if move_val > best_val:
                best_val = move_val
                best_move = i

    exec_time = (time.time() - start_time) * 1000
    return best_move, best_val, exec_time


def print_board(board):
    for row in range(0, 9, 3):
        print("  ", " | ".join(board[row:row+3]))
        if row < 6:
            print("  ---+---+---")


if __name__ == "__main__":
    # Sample mid-game Tic-Tac-Toe board state
    sample_board = [
        'X', 'O', 'X',
        'O', 'O', ' ',
        ' ', ' ', 'X'
    ]

    print("=== Minimax with Alpha-Beta Pruning (Tic-Tac-Toe) ===")
    print("Current Board State:")
    print_board(sample_board)

    move_idx, score, elapsed = find_best_move(sample_board)
    sample_board[move_idx] = 'X'

    print(f"\nOptimal Move for 'X' at Cell Index: {move_idx} (Score: {score})")
    print("Board After AI Optimal Move:")
    print_board(sample_board)
    print(f"Execution Time: {elapsed:.4f} ms")
