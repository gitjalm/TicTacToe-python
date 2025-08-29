board = []

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

def update_board(row, col):
    if board[row-1][col-1] == "-":
        board[row-1][col-1] = "X"
        display_board()
    else:
        print("Cell already taken. Try again.")
        display_board()
    make_move()

def make_move():
    move = input("Enter your move (example: 1 2 for row 1 column 2): ")
    row = int(move[0])
    col = int(move[2])
    if len(move) != 3:
        print("Invalid Input. Please enter a two-digit number.")
        display_board()
        make_move()
        return
    if row > 3 or col > 3:
        print("Invalid Input. Please enter a number between 1 and 3.")
        display_board()
        make_move()
        return
    update_board(row, col)
    

def main():
    print("Welcome to Tic Tac Toe!")
    play = input("Do you want to play? (Y/N): ")
    if play.lower() == 'y':
        initialize_board()
        display_board()
        make_move()
    elif play.lower() == 'n':
        print("Maybe next time!")
    else:
        print("Invalid Input. Please enter Y or N.")
    

if __name__ == "__main__":
    main()