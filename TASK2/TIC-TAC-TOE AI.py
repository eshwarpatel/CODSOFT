import math

board = [' ' for _ in range(9)]

def print_board():
    print("\n")
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print("---|---|---")
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print("---|---|---")
    print(f' {board[6]} | {board[7]} | {board[8]} ')
    print("\n")

def check_winner(player):
    win_conditions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    return any(board[a] == board[b] == board[c] == player for a,b,c in win_conditions)

def minimax(is_maximizing):
    if check_winner('O'):
        return 10
    if check_winner('X'):
        return -10
    if ' ' not in board:
        return 0
    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -math.inf
    best_move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = 'O'

def human_move():
    while True:
        move = input("Your turn (1-9): ")
        if move.isdigit() and int(move) in range(1, 10):
            move = int(move) - 1
            if board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print("This spot is taken!")
        else:
            print("Invalid input. Enter a number between 1-9.")

def play_game():
    print("\nWelcome to Tic-Tac-Toe!")
    print_board()
    while True:
        if ' ' not in board:
            print("It's a draw!")
            break
        if check_winner('O'):
            print("AI wins! Better luck next time.")
            break
        if check_winner('X'):
            print("You win! Congratulations!")
            break
        human_move()
        ai_move()
        print_board()

play_game()