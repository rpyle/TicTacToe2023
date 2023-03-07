team_name = 'McFarland'
strategy_name = 'Best Stratagy'
strategy_description = 'Play the next most strategic location.'

def move(player, board, score): #required
 
  #------------------------ resets stratagy values -----------------------------
  r = 0
  c = 0
  turns = 0
  enemy = 0
  spot1 = False
  spot2 = False
  spot3 = False
  spot4 = False
  spot5 = False
  spot6 = False
  spot7 = False
  spot8 = False
  spot9 = False
  if (player == 'X'):
    enemy = 'O'
  if (player == 'O'):
    enemy = 'X'
  #----------------------- checks to see what turn the program is on -----------------------
  for spaces in range(9):
    if (board[r][c] == player):
      turns += 1
      c = c + 1
      if c > 2:
        c = 0
        r = r + 1
    else:
      c = c + 1
      if c > 2:
        c = 0
        r = r + 1
  #---------------------Checks what spots I or the other person have taken-----------------
  if (board[0][0] == player):
    spot1 = True
  if (board[0][1] == player):
    spot2 = True
  if (board[0][2] == player):
    spot3 = True
  if (board[1][0] == player):
    spot4 = True
  if (board[1][1] == player):
    spot5 = True
  if (board[1][2] == player):
    spot6 = True
  if (board[2][0] == player):
    spot7 = True
  if (board[2][1] == player):
    spot8 = True
  if (board[2][2] == player):
    spot9 = True
  if (board[0][0] == enemy):
    spot1 = enemy
  if (board[0][1] == enemy):
    spot2 = enemy
  if (board[0][2] == enemy):
    spot3 = enemy
  if (board[1][1] == enemy):
    spot4 = enemy
  if (board[1][2] == enemy):
    spot5 = enemy
  if (board[1][0] == enemy):
    spot6 = enemy
  if (board[2][0] == enemy):
    spot7 = enemy
  if (board[2][1] == enemy):
    spot8 = enemy
  if (board[2][2] == enemy):
    spot9 = enemy
  #--------------------------------------- plays stratagy ------------------------------------
 #------------checks for any winning moves---------------
#-------------takes spot if two are near each other---------------
  elif (spot1):
    if (spot2 and board[0][2] == ' '):
      r = 0
      c = 2
    elif (spot5 and board[2][2] == ' '):
      r = 2
      c = 2
    elif (spot4 and board[2][0] == ' '):
      r = 2
      c = 0
  elif (spot3):
    if (spot2 and board[0][0] == ' '):
      r = 0
      c = 0
    elif (spot5 and board[2][0] == ' '):
      r = 2
      c = 0
    elif (spot6 and board[2][2] == ' '):
      r = 2
      c = 2
  elif (spot7):
    if (spot4 and board[0][0] == ' '):
      r = 0
      c = 0
    elif (spot5 and board[0][2] == ' '):
      r = 0
      c = 2
    elif (spot8 and board[2][2] == ' '):
      r = 2
      c = 2
  elif (spot9):
    if (spot8 and board[2][0] == ' '):
      r = 2
      c = 0
    elif (spot5 and board[0][0] == ' '):
      r = 0
      c = 0
    elif (spot6 and board[0][2] == ' '):
      r = 0
      c = 2


 #-------------- tries to set up for winning move----------
  if (spot1 == enemy):
    if (spot2 == enemy and board[0][2] == ' '):
      r = 0
      c = 2
    elif (spot5 == enemy and board[2][2] == ' '):
      r = 2
      c = 2
    elif (spot4 == enemy and board[2][0] == ' '):
      r = 2
      c = 0
  elif (spot3 == enemy):
    if (spot2 == enemy and board[0][0] == ' '):
      r = 0
      c = 0
    elif (spot5 == enemy and board[2][0] == ' '):
      r = 2
      c = 0
    elif (spot6 == enemy and board[2][2] == ' '):
      r = 2
      c = 2
  elif (spot7 == enemy):
    if (spot4 == enemy and board[0][0] == ' '):
      r = 0
      c = 0
    elif (spot5 == enemy and board[0][2] == ' '):
      r = 0
      c = 2
    elif (spot8 == enemy and board[2][2] == ' '):
      r = 2
      c = 2
  elif (spot9 == enemy):
    if (spot8 == enemy and board[2][0] == ' '):
      r = 2
      c = 0
    elif (spot5 == enemy and board[0][0] == ' '):
      r = 0
      c = 0
    elif (spot6 == enemy and board[0][2] == ' '):
      r = 0
      c = 2
  else:
    if (turns == 0): # Checks middle
      if (board[1][1] == ' '):
       r = 1
       c = 1
      else:
        if (board[0][1] == ' '):
         r = 0
         c = 1
         spot2 = True
        elif (board[1][0] == ' '):
         r = 1
         c = 0
         spot4 = True
        elif (board[1][2] == ' '):
         r = 1
         c = 2
         spot6 = True
        elif (board[2][1] == ' '):
         r = 2
         c = 1
         spot8 = True
    if (turns == 1): # checks edge spots
      if (board[0][1] == ' '):
         r = 0
         c = 1
      elif (board[1][0] == ' '):
         r = 1
         c = 0
      elif (board[1][2] == ' '):
        r = 1
        c = 2
      elif (board[2][1] == ' '):
        r = 2
        c = 1
    
    if (turns == 2): # checks corner spots near last spot taken
      if (spot2 == True or spot6 == True):
        if (board[0][2] == ' '):
         r = 0
         c = 2
      elif (spot2 == True or spot4 == True):
        if (board[0][0] == ' '):
         r = 0
         c = 0
      elif (spot4 == True or spot8 ==True):
        if (board[2][0] == ' '):
         r = 2
         c = 0
      elif (spot6 == True or spot8 == True):
        if (board[2][2] == ' '):
         r = 2
         c = 2
      if (spot1 == False and spot3 == False and spot7 == False and spot9== False):
        if (board[0][1] == ' '):
          r = 0
          c = 1
        elif (board[1][0] == ' '):
          r = 1
          c = 0
        elif (board[1][2] == ' '):
          r = 1
          c = 2
        elif (board[2][1] == ' '):
          r = 2
          c = 1
  
  
  return r, c #required