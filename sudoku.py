# board
# sufficient numbers4
# unique numbers in row and cols
# 4 --> 2
# 9 --> 3
import math


board = int(input("what size do you want"))
r_b = int(board**0.5)

if type(math.isqrt(board)) == int:
    sb = []
    for i in range(board):
        l1 = []
        for j in range(board):
            l1.append(0)
        sb.append(l1)
        del(l1)


def user_ip():
    row = int(input("what row you want to play: "))
    col = int(input("what col you want to play: "))

    num = int(input("Enter Number: "))
    # block max limit==board/2
    # checker while input
    # 30% of round(board**2)

    return row, col, num


limit = round(board**2 * 0.3)


def checker(row, col, num):
    '''
    to check if thhe number repeats in a 

    block, 
    row and
    column
    '''
    r_counter = 0
    for i in range(board):
        if i != col:
            if sb[row][i] == num:
                r_counter += 1

    if r_counter >= 1:
        print('entered number already exists')
        return False
    else:
        return True
    c_counter = 0
    for i in range(board):
        if i != row:
            if sb[i][col] == num:
                c_counter += 1
    if c_counter >= 1:
        print('entered number already exists')
        return False
    else:
        return True


def block(num):
    for i in range(1, r_b+1):
        pre = r_b*(i-1)
        post = r_b*(i)
        foo = 0
        for j in range(pre, post):
            for k in range(pre, post):
                if sb[j][k] == num:
                    foo += 1

                if foo > 1:
                    return False


bar = 0
while bar < limit:
    row, col, num = user_ip()
    if checker(row, col, num):
        block(num)
        print(f'chal gaya...{num}')
        print(sb)
        bar += 1
