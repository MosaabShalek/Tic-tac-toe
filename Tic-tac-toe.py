# functions

def print_board():
    for i in range(9):
        print(board[i], end = ' ')
        if (i+1)%3 == 0:
            print()

def play():
    print('player {} turn!!'.format(turn))
    num = int(input('choose a cell from 1 to 9: '))
    if num == board[num-1]:
        board[num-1] = turn

def check_winner():
    winning = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in range(8):
        win = True
        for k in range(3):
            if board[winning[i][k]] != turn:
                win = False
        if win == True:
            return True
    
    return False

def flip_turn():
    if turn == 'X':
        return 'O'
    else:
        return 'X'
        

# one time code

board = [1,2,3,4,5,6,7,8,9]
turn = 'X'
print_board()

# game loop

for i in range(9):
    play()
    print_board()
    if check_winner() == True:
        print('player {} won!!'.format(turn))
        break
    turn = flip_turn()
if check_winner() == False:
    print('it is a Tie!!!!')
