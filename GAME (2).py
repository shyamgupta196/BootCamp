from day3 import checker, all_same
import pandas as pd
# overplay
# wins done
size = int(input("What should be the board size: "))


def make_board():
    global board
    board = []
    for i in range(size):
        local_list = []
        for i in range(size):
            local_list.append(0)
        board.append(local_list)


make_board()


def display():
    for row_no, row in enumerate(board):
        print(row_no, "  ", *row)


def turns(player):
    print(f"its {player} turn")
    row = int(input("what row you want to play: "))
    col = int(input("what col you want to play: "))
    return row, col


game = True
win = False
i = 0
while game:
    no_of_players = 2
    # since we are using while loops now
    # the game wont terminate automatically INFINITE LOOP me fasega
    # hence we check the condition

    # / diagonal
    diags = []
    for idx, reverse_idx in enumerate(reversed(range(len(board)))):
        diags.append(board[idx][reverse_idx])
    if all_same(diags):
        print(f"Player {diags[0]} has won Diagonally (/)")
        # continuer()
        break
    # \ diagonal
    diags = []
    for ix in range(len(board)):
        diags.append(board[ix][ix])
    if all_same(diags):
        print(f"Player {diags[0]} has won Diagonally (\\)")
        # continuer()
        break

    if i == int(len(board[0]) ** 2):
        break
    if i % 2 == 0:
        assign = False
        while not assign:
            try:
                row, col = turns("X")
                if (board[row][col] == 0) and (board[row][col] != "X"):
                    board[row][col] = "X"
                    display()
                    i += 1
                    assign = True
                else:
                    print("Try Again...")
                    turns("X")
            except:
                print("Oops! something went wrong")
        if checker(board, "X") == True:
            # continuer()
            break

    else:
        assign = False
        while not assign:
            try:
                row, col = turns("O")
                if (board[row][col] == 0) and (board[row][col] != "X"):
                    board[row][col] = "O"
                    display()
                    i += 1
                    assign = True
                else:
                    print("Try Again...")
                    turns("O")
            except:
                print("Oops! something went wrong")
        if checker(board, "O") == True:
            # continuer()
            break
