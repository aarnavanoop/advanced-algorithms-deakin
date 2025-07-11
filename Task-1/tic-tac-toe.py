import math

# Define the players
PLAYER = 'O'
AI = 'X'

def print_board(board):

    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    """Checks if the specified player has won."""

    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    return [player, player, player] in win_conditions

def get_empty_cells(board):

    empty_cells = []
    for r in range(3):
        for c in range(3):
            if board[r][c] == " ":
                empty_cells.append((r, c))
    return empty_cells

def minimax(board, depth, is_maximizing):

    if check_winner(board, AI):
        return 10
    if check_winner(board, PLAYER):
        return -10
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for r, c in get_empty_cells(board):
            board[r][c] = AI
            score = minimax(board, depth + 1, False)
            board[r][c] = " " 
            best_score = max(score, best_score)
        return best_score
    else: # Minimizing
        best_score = math.inf
        for r, c in get_empty_cells(board):
            board[r][c] = PLAYER
            score = minimax(board, depth + 1, True)
            board[r][c] = " " 
            best_score = min(score, best_score)
        return best_score