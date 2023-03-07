team_name = 'Santo'
strategy_name = 'Santo Strategy'
strategy_description = 'more time blocking, less time doing'

import random

#def print_board(board):
 #print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
 #print('-+-+-')
  #print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  #print('-+-+-')
  #print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])

#Horizontal (0,0 0,1 0,2) (1,0 1,1 1,2) (2,0 2,1 2,2) 
#Vertical (0,0 1,0 2,0) (0,1 1,1 2,1) (0,2 1,2 2,2)
#Diagonal (0,0 1,1 2,2) (0,2 1,1 2,0)
  
#Check Opps Placing on board
#Figure out where the placement is
#Block
#tl = board[0][0]
#tr = board[0][2]
#bl = board[2][0]
#br = board[2][2]
def move(player, board, score):
  enemy = not player and not ' '
  if enemy == board[0][0] and board[0][1]:
    r = 0
    c = 2
    
    return r, c
  elif enemy == board[0][1] and board[0][2]:
    r = 0
    c = 0
    
    return r, c
  elif enemy == board[0][0] and board[0][2]:
    r = 0
    c = 1
    
    return r, c
  elif enemy == board[1][0] and board[1][1]:
    r = 1
    c = 2
    
    return r, c
  elif enemy == board[1][1] and board[1][2]:
    r = 1
    c = 0
    
    return r, c
  elif enemy == board[1][0] and board[1][2]:
    r = 1
    c = 1
    
    return r, c
  elif enemy == board[2][0] and board[2][1]:
    r = 1
    c = 2
    
    return r, c
  elif enemy == board[2][1] and board[2][2]:
    r = 1
    c = 0
    
    return r, c
  elif enemy == board[2][0] and board[2][2]:
    r = 1
    c = 1
    
    return r, c
    #diagonaisl
  elif enemy == board[0][0] and board[2][2]:
    r = 1
    c = 1
    
    return r, c
  elif enemy == board[0][0] and board[1][1]:
    r = 2
    c = 2
    
    return r, c
  elif enemy == board[1][1] and board[2][2]:
    r = 0
    c = 0
    
    return r, c
  elif enemy == board[0][2] and board[2][0]:
    r = 1
    c = 1
    
    return r, c
  elif enemy == board[0][2] and board[1][1]:
    r = 2
    c = 0
    
    return r, c
  elif enemy == board[1][1] and board[2][0]:
    r = 0
    c = 2
    
    return r, c
  else:
   r = 1
   c = 1
   while board[r][c] != ' ':
    r = random.randint(0,2)
    c = random.randint(0,2)
  
  #
  #print_board(board)
  return r, c


 

