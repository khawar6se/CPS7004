import math

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def get_empty_cells(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

def minimax(board, depth, is_maximizing):
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for r, c in get_empty_cells(board):
            board[r][c] = "O"
            score = minimax(board, depth + 1, False)
            board[r][c] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for r, c in get_empty_cells(board):
            board[r][c] = "X"
            score = minimax(board, depth + 1, True)
            board[r][c] = " "
            best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for r, c in get_empty_cells(board):
        board[r][c] = "O"
        score = minimax(board, 0, False)
        board[r][c] = " "
        if score > best_score:
            best_score = score
            move = (r, c)
    return move

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print("You are 'X'. Computer is 'O'.")
    print_board(board)

    while True:
        # Player move
        while True:
            try:
                row = int(input("Enter your row (0-2): "))
                col = int(input("Enter your column (0-2): "))
                if board[row][col] != " ":
                    print("Cell already taken. Try again.")
                    continue
                board[row][col] = "X"
                break
            except (ValueError, IndexError):
                print("Invalid input. Enter numbers from 0 to 2.")

        print_board(board)
        if check_winner(board, "X"):
            print("🎉 You win!")
            break
        if is_full(board):
            print("It's a tie!")
            break

        # AI move
        print("Computer is making a move...")
        r, c = best_move(board)
        board[r][c] = "O"
        print_board(board)

        if check_winner(board, "O"):
            print("😢 You lost. Computer wins.")
            break
        if is_full(board):
            print("It's a tie!")
            break

# Run the game
tic_tac_toe()

