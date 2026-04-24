import math

# Board setup
board = [" " for _ in range(9)]

def print_board():
    print()
    for i in range(3):
        print("|".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-"*5)
    print()

def check_winner(player):
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],  # rows
        [0,3,6],[1,4,7],[2,5,8],  # cols
        [0,4,8],[2,4,6]           # diagonals
    ]
    for pos in win_positions:
        if all(board[i] == player for i in pos):
            return True
    return False

def is_draw():
    return " " not in board

# 🔥 Minimax Algorithm
def minimax(is_maximizing):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

# AI Move
def ai_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"

# Game Loop
def play():
    print("Positions are numbered 1 to 9")
    print_board()

    while True:
        # Human move
        pos = int(input("Enter your move (1-9): ")) - 1
        if board[pos] != " ":
            print("Invalid move!")
            continue
        board[pos] = "X"

        print_board()
        if check_winner("X"):
            print("You win!")
            break
        if is_draw():
            print("Draw!")
            break

        # AI move
        print("AI is thinking...")
        ai_move()
        print_board()

        if check_winner("O"):
            print("AI wins!")
            break
        if is_draw():
            print("Draw!")
            break

play()