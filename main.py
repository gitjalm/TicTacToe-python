board = []

def initialize_board():
    board.clear()
    for _ in range(3):
        board.append(["x", "x", "x"])

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
    

def main():
    print("Welcome to Tic Tac Toe!")
    play = input("Do you want to play? (Y/N): ")
    if play.lower() == 'y':
        initialize_board()
        display_board()
    elif play.lower() == 'n':
        print("Maybe next time!")
    else:
        print("Invalid Input. Please enter Y or N.")
    

if __name__ == "__main__":
    main()