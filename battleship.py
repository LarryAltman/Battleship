from random import randint
# populate list with 5 rows & columns
board = []
for x in range(0, 5):
    board.append(["O"] * 5)
# join the values within the quotation marks
def print_board(board):
    for row in board:
        print(" ".join(row))
# place ship on the board
ship_row = randint(0, 4)
ship_col = randint(0, 4)
gameWin = False
# loop until the game winning condition is met
while gameWin == False:
    print_board(board)
    print("Ship location =", ship_row, ",", ship_col)
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Column: "))

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sank my battleship!")
        gameWin = True
    elif guess_row not in range(5) or guess_col not in range(5):
        print("Oops, that's not even in the ocean.\n")
    elif board[guess_row][guess_col] == "X":
        print("You guessed that one already.\n")
    else:
        print("You missed my battleship!\n")
        board[guess_row][guess_col] = "X"
