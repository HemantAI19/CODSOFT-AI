from game_logic import initialize_board, display_board, check_win, is_board_full, find_best_move

def play_game():
    board = initialize_board()
    print("Tic-Tac-Toe Game: You are 'O' and the AI is 'X'.\n")

    while True:
        display_board(board)
        
        try:
            row, col = map(int, input("Enter your move (row and column as space-separated numbers): ").split())
            if board[row][col] != " ":
                print("Invalid move. Try again.")
                continue
            board[row][col] = "O"
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column numbers between 0 and 2.")
            continue
        
        if check_win(board, "O"):
            display_board(board)
            print("You win!")
            break
        elif is_board_full(board):
            display_board(board)
            print("It's a draw!")
            break
        
        print("AI's move...")
        ai_move = find_best_move(board)
        board[ai_move[0]][ai_move[1]] = "X"
        
        if check_win(board, "X"):
            display_board(board)
            print("AI wins!")
            break
        elif is_board_full(board):
            display_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
