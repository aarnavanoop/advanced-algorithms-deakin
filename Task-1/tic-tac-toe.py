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

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

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
    
def find_best_move(board):

    best_score = -math.inf
    best_move = None
    for r, c in get_empty_cells(board):
        board[r][c] = AI
        score = minimax(board, 0, False)
        board[r][c] = " " # Backtrack
        if score > best_score:
            best_score = score
            best_move = (r, c)
    return best_move

def play_game():

    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = PLAYER 

    while True:
        print_board(board)

        if current_player == PLAYER:
            try:
                row = int(input("Enter row (0, 1, or 2): "))
                col = int(input("Enter column (0, 1, or 2): "))
                if board[row][col] == " ":
                    board[row][col] = PLAYER
                    if check_winner(board, PLAYER):
                        print_board(board)
                        print("Congratulations, you win!")
                        break
                    current_player = AI
                else:
                    print("That spot is already taken.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter a number between 0 and 2.")
        else: # AI's turn
            print("AI is thinking...")
            move = find_best_move(board)
            if move:
                board[move[0]][move[1]] = AI
                if check_winner(board, AI):
                    print_board(board)
                    print("AI wins!")
                    break
                current_player = PLAYER
        
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break


if __name__ == "__main__":
    play_game()