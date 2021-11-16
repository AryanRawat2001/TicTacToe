#Hi There!
player = 0 
BoardPos = None

TicTacBoard = {1:'  ',2:'  ',3:'  ',  
               4:'  ',5:'  ',6:'  ',
               7:'  ',8:'  ',9:'  '}
 
def printBoard(board):
    print(board[1]+ '|'+board[2]+'|'+board[3])
    print(' _.__._') 
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(' _.__._') 
    print(board[7]+'|'+board[8]+'|'+board[9])

def winnerDecider(w):
    if w[1] == w[2] and w[2]== w[3] and w[1]== 'X':
        return 1 
    elif w[4] == w[5] and w[5]== w[6] and w[4]== 'X':
        return 1    
    elif w[7] == w[8] and w[8]== w[9] and w[7]== 'X':
        return 1
    elif w[1] == w[4] and w[4]== w[7] and w[1]== 'X':
        return 1
    elif w[2] ==w[5] and w[5]== w[8] and w[2]== 'X':
        return 1
    elif w[3] ==w[6] and w[6]== w[9] and w[3]== 'X':
        return 1
    elif w[1] ==w[5] and w[5]== w[9] and w[1]== 'X':
        return 1
    elif w[3] ==w[5] and w[5]== w[7] and w[3]== 'X':
        return 1
    elif w[1] ==  w[2] and w[2]==w[3]and w[1]=='O':
        return 0
    elif w[4] == w[5] and w[5]== w[6] and w[4]== 'O':
        return 0   
    elif w[7] == w[8] and w[8]== w[9] and w[7]== 'O':
        return 0
    elif w[1] == w[4] and w[4]== w[7] and w[1]== 'O':
        return 0
    elif w[2] ==w[5] and w[5]== w[8] and w[2]== 'O':
        return 0
    elif w[3] ==w[6] and w[6]== w[9] and w[3]== 'O':
        return 0
    elif w[1] ==w[5] and w[5]== w[9] and w[1]== 'O':
        return 0
    elif w[3] ==w[5] and w[5]== w[7] and w[3]== 'O':
        return 0
print('This Is Your TicTacToe Board:')
printBoard(TicTacBoard)

for chance in range(1,10):
   
    if player == 0:
        BoardPos=int(input('Player 1 , Where do you want to move?:'))
        TicTacBoard[BoardPos]= 'X'
        player = 1
    elif player == 1:
        BoardPos=int(input('Player 2 , Where do you want to move?:'))
        TicTacBoard[BoardPos]= 'O'
        player = 0

    printBoard(TicTacBoard)

    if winnerDecider(TicTacBoard)==0:
        print('Player 2 is the Winner!!')
        break
    elif winnerDecider(TicTacBoard) == 1 :
        print('Player 1 is the winner!!')
        break
if not winnerDecider(TicTacBoard)==1 or winnerDecider(TicTacBoard)== 0 :
    print('Its a Draw :(')
    

 
    
    



