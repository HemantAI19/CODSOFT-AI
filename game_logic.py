import random
def initialize_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def display_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_win(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]):  
            return True
        if all([board[j][i] == player for j in range(3)]):  
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:  
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:  
        return True
    return False

def is_board_full(board):
    return all([cell != " " for row in board for cell in row])

def minimax(board, depth, is_maximizing, alpha, beta):
    if check_win(board, "X"):
        return 1
    elif check_win(board, "O"):
        return -1
    elif is_board_full(board):
        return 0
    
    if is_maximizing:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"  
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = " "  
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"  
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = " "  
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def find_best_move(board):
    best_move = None
    best_val = float('-inf')
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"  
                move_val = minimax(board, 0, False, float('-inf'), float('inf'))
                board[i][j] = " "  
                
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)
                    
    return best_move
