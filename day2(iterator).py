## WE ARE MAKING AN ITERATOR / COUNTER 
board = [[0, 0, 0],
[0, 0, 0], 
[0, 0, 0]]

def display():
    for row_no,row in enumerate(board):
        print(row_no,'  ',*row)

for i in range(len(board)**2):
    no_of_players = 2
    if i%2==0:
        print('its X turn')
        row = int(input('what row you want to play: '))
        col = int(input('what col you want to play: '))
        board[row][col] = 'X'
        display()
    else:
        print('its O turn')
        row = int(input('what row you want to play: '))
        col = int(input('what col you want to play: '))
        board[row][col] = 'O'
        display()
