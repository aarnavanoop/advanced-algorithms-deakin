import math

# Define the players
PLAYER = 'O'
AI = 'X'

def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
