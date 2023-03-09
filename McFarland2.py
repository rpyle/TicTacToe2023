team_name = 'McFarland'
strategy_name = 'Best Stratagy'
strategy_description = 'Play the next most strategic location.'


def move(player, board, score): #required
 
  #------------------------ resets stratagy values ---------------------------
  r = 0
  c = 0
  t = 0
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
  if (spot1):
    if (spot2 and board[0][2] == ' '):
      r = 0
      c = 2
    else:
      t += 1
    if (spot5 and t == 1 and board[2][2] == ' '):
      r = 2
      c = 2
    else:
      t += 1
    if (spot4 and t == 2 and board[2][0] == ' '):
      r = 2
      c = 0
    else:
      t += 1
  if (spot3 and t == 3):
    if (spot2 and board[0][0] == ' '):
      r = 0
      c = 0
    else:
      t += 1
    if (spot5 and t ==4 and board[2][0] == ' '):
      r = 2
      c = 0
    else:
      t += 1
    if (spot6 and t == 5 and board[2][2] == ' '):
      r = 2
      c = 2
    else:
      t += 1
  if (spot7 and t == 6):
    if (spot4 and board[0][0] == ' '):
      r = 0
      c = 0
    else:
      t += 1
    if (spot5 and t == 7 and board[0][2] == ' '):
      r = 0
      c = 2
    else:
      t += 1
    if (spot8 and t == 8 and board[2][2] == ' '):
      r = 2
      c = 2
    else:
      t += 1
  if (spot9 and t == 9):
    if (spot8 and board[2][0] == ' '):
      r = 2
      c = 0
    else:
      t += 1
    if (spot5 and t == 10 and board[0][0] == ' '):
      r = 0
      c = 0
    else:
      t += 1
    if (spot6 and t == 11 and board[0][2] == ' '):
      r = 0
      c = 2
    else:
      t += 1


 #-------------- tries to set up for winning move----------
  if (spot5 and t == 12):
    if (spot2 and board[2][1] == ' '):
      r = 2
      c =1
    else:
      t += 1
    if (spot4 and t == 13 and board[1][2] == ' '):
      r = 1
      c =2
    else:
      t += 1
    if (spot6 and t == 14 and board[1][0] == ' '):
      r = 1
      c =0
    else:
      t += 1
    if (spot8 and t == 15 and board[0][1] == ' '):
      r = 0
      c =1
    else:
      t += 1
  if (spot1 == enemy and t == 16):
    if (spot2 == enemy and board[0][2] == ' '):
      r = 0
      c = 2
    else:
      t += 1
    if (spot5 == enemy and t == 17 and board[2][2] == ' '):
      r = 2
      c = 2
    else:
      t += 1
    if (spot4 == enemy and t == 18 and board[2][0] == ' '):
      r = 2
      c = 0
    else:
      t += 1
  if (spot3 == enemy and t == 19):
    if (spot2 == enemy and board[0][0] == ' '):
      r = 0
      c = 0
    else:
      t += 1
    if (spot5 == enemy and t == 20 and board[2][0] == ' '):
      r = 2
      c = 0
    else:
      t += 1
    if (spot6 == enemy and t == 21 and board[2][2] == ' '):
      r = 2
      c = 2
    else:
      t += 1
  if (spot7 == enemy and t == 22):
    if (spot4 == enemy and board[0][0] == ' '):
      r = 0
      c = 0
    else:
      t += 1
    if (spot5 == enemy and t == 23 and board[0][2] == ' '):
      r = 0
      c = 2
    else:
      t += 1
    if (spot8 == enemy and t == 24 and board[2][2] == ' '):
      r = 2
      c = 2
    else:
      t += 1
  if (spot9 == enemy and t == 25):
    if (spot8 == enemy and board[2][0] == ' '):
      r = 2
      c = 0
    else:
      t += 1
    if (spot5 == enemy and t == 26 and board[0][0] == ' '):
      r = 0
      c = 0
    else:
      t += 1
    if (spot6 == enemy and t == 27 and board[0][2] == ' '):
      r = 0
      c = 2
    else:
      t += 1
  if (spot5 == enemy and t == 28):
    if (spot2 == enemy and board[2][1] == ' '):
      r = 2
      c =1
    else:
      t += 1
    if (spot4 == enemy and t == 29 and board[1][2] == ' '):
      r = 1
      c =2
    else:
      t += 1
    if (spot6 == enemy and t == 30 and board[1][0] == ' '):
      r = 1
      c =0
    else:
      t += 1
    if (spot8 == enemy and t == 31 and board[0][1] == ' '):
      r = 0
      c =1
    else:
      t += 1
  else:
      if (board[1][1] == ' '):
       r = 1
       c = 1
      else:
       t += 1
      if (spot2 == True or spot6 == True):
         if (board[0][2] == ' ' and t == 32):
           r = 0
           c = 2
         else:
           t += 1
      else:
       t += 1
      if (spot2 == True and spot4 == True):
        if (board[0][0] == ' ' and t == 33):
           r = 0
           c = 0
        else:
          t += 1
      else:
       t += 1
      if (spot4 == True and spot8 ==True):
        if (board[2][0] == ' ' and t == 34):
         r = 2
         c = 0
        else:
          t += 1
      else:
       t += 1
      if (spot6 == True and spot8 == True):
        if (board[2][2] == ' ' and t == 35):
         r = 2
         c = 2
        else:
          t += 1
      else:
       t += 1
      if (t == 36):
        if (board[2][2] == ' '):
         r = 2
         c = 2
          
        if (board[0][1] == ' '):
         r = 0
         c = 1
        if (board[1][0] == ' '):
         r = 1
         c = 0
        if (board[1][2] == ' '):
         r = 1
         c = 2
        if (board[2][1] == ' '):
         r = 2
         c = 1

 
    
  return r, c #required