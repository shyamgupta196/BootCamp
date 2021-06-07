##board = [['X', 'X', 'X'],
##[0, 0, 0],
##[0, 0, 0]]
        
def checker(board, player):
    """
    checks only for horizontal and vertical
    """
    for i in range(len(board[0])):
        vertical = []
        for j in range(len(board[0])):
            vertical.append(board[j][i])
            # print(vertical)
            if board[i].count(player) == len(board[0]):
                print(f"winner is {player} horizontally (---)")
                return True
            elif vertical.count(player) == len(board[0]):
                print(f"winner is {player} vertically (|)")
                return True


def all_same(l):
    if l.count(l[0]) == len(l) and l[0] != 0:
        return True
    else:
        return False


# / diagonal
# diags = []
# for idx, reverse_idx in enumerate(reversed(range(len(board)))):
#     diags.append(board[idx][reverse_idx])

# if all_same(diags):
#     print(f"Player {diags[0]} has won Diagonally (/)")

# # \ diagonal
# diags = []
# for ix in range(len(board)):
#     diags.append(board[ix][ix])

# if all_same(diags):
#     print(f"Player {diags[0]} has won Diagonally (\\)")

# i used this website for diags condition
# since rest of the conditions are done
# i do not use copy those -- from this site
### checkout https://pythonprogramming.net/wrapping-up-tic-tac-toe-learn-python-3-tutorials/
###NEVER FORGET TO REFERENCE OR GIVE CREDIT TO THE PERSON who helped you with code
## or if you have used a part of it



## chklist  can be also used


def chkList(lst):
    return len(set(lst)) == 1
