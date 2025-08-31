board = []
moves = 0

def initialize_board():
    board.clear()
    for _ in range(3):
        board.append(["-", "-", "-"])

def display_board():
    time = 1
    row = str(time)
    print("  1 2 3 ")
    for x in board:
        for y in x:
            row += " " + y
        time += 1
        print(row)
        row = str(time)

def update_board(player, player1, player2, row, col):
    global moves
    if board[row-1][col-1] == "-":
        if player == "player1":
            board[row-1][col-1] = "X"
            moves += 1
        else:
            board[row-1][col-1] = "O"
            moves += 1
        display_board()
    else:
        print("Cell already taken. Try again.")
        display_board()
    make_move(player1, player2)

def make_move(player1, player2):
    global moves
    if moves % 2 == 0:
        move = input(f"{player1} make your move (example: 1 2 for row 1 column 2): ")
        player = "player1"
    else:
        move = input(f"{player2} make your move (example: 1 2 for row 1 column 2): ")
        player = "player2"
    row = int(move[0])
    col = int(move[2])
    if len(move) != 3:
        print("Invalid Input. Please enter a two-digit number.")
        display_board()
        make_move(player1, player2)
        return
    if row > 3 or col > 3:
        print("Invalid Input. Please enter a number between 1 and 3.")
        display_board()
        make_move(player1, player2)
        return
    update_board(player, player1, player2, row, col)
    

def main():
    print("Welcome to Tic Tac Toe!")
    play = input("Do you want to play? (Y/N): ")
    player1 = input("Enter name for Player 1 (X): ")
    player2 = input("Enter name for Player 2 (O): ")
    if play.lower() == 'y':
        initialize_board()
        display_board()
        make_move(player1, player2)
    elif play.lower() == 'n':
        print("Maybe next time!")
    else:
        print("Invalid Input. Please enter Y or N.")
    

if __name__ == "__main__":
    main()