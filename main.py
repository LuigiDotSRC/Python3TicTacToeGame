import tkinter as tk 
from tkinter import ttk

def init():
  print('''
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        Welcome to Python Tic Tac Toe 
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    ''')

def drawinit():
  print('''
     A1 | A2 | A3
    ____|____|____
     B1 | B2 | B3
    ____|____|____
     C1 | C2 | C3 
        |    |    

    ''')

def drawgame(moves):
  A1 = A2 = A3 = B1 = B2 = B3 = C1 = C2 = C3 = " "

  for i in moves:
    if (i[:2] == "P1"):
      move = i[2:4]

      if (move == "A1"):
        A1 = "X"
      elif (move == "A2"):
        A2 = "X"
      elif (move == "A3"):
        A3 = "X"
      elif (move == "B1"):
        B1 = "X"
      elif (move == "B2"):
        B2 = "X"
      elif (move == "B3"):
        B3 = "X"
      elif (move == "C1"):
        C1 = "X"
      elif (move == "C2"):
        C2 = "X"
      elif (move == "C3"):
        C3 = "X"

    elif (i[:2] == "P2"):
      move = i[2:4]

      if (move == "A1"):
        A1 = "O"
      elif (move == "A2"):
        A2 = "O"
      elif (move == "A3"):
        A3 = "O"
      elif (move == "B1"):
        B1 = "O"
      elif (move == "B2"):
        B2 = "O"
      elif (move == "B3"):
        B3 = "O"
      elif (move == "C1"):
        C1 = "O"
      elif (move == "C2"):
        C2 = "O"
      elif (move == "C3"):
        C3 = "O"

  print("         |     |     ")
  print("      " + A1 + "  |  " + A2 + "  |  " + A3)
  print("    _____|_____|_____")

  print("         |     |     ")
  print("      " + B1 + "  |  " + B2 + "  |  " + B3)
  print("    _____|_____|_____")

  print("         |     |     ")
  print("      " + C1 + "  |  " + C2 + "  |  " + C3)
  print("         |     |     ")
  
def wincondition(moves):
  p1moves = []
  p2moves = []

  for i in moves:
    if(i[:2] == "P1"):
      p1moves.append(i[2:4])
    elif(i[:2] == "P2"):
      p2moves.append(i[2:4])

  p1rowA = p1rowB = p1rowC = 0
  p1col1 = p1col2 = p1col3 = 0
  p2rowA = p2rowB = p2rowC = 0
  p2col1 = p2col2 = p2col3 = 0
  middle = A1 = A3 = C1 = C3 = 0

  for i in p1moves:
    if(i[:1] == "A"): 
      p1rowA += 1 
    elif(i[:1] == "B"):
      p1rowB += 1 
    elif(i[:1] == "C"):
      p1rowC += 1

    if(i[1:2] == "1"): 
      p1col1 += 1 
    elif(i[1:2] == "2"):
      p1col2 += 1 
    elif(i[1:2] == "3"):
      p1col3 += 1

    if(i == "B2"):
      middle = 1
    elif(i == "A1"):
      A1 = 1
    elif(i == "A3"):
      A3 = 1
    elif(i == "C1"):
      C1 = 1
    elif(i == "C3"):
      C3 = 1

  for i in p2moves:
    if(i[:1] == "A"): 
      p2rowA += 1 
    elif(i[:1] == "B"):
      p2rowB += 1 
    elif(i[:1] == "C"):
      p2rowC += 1

    if(i[1:2] == "1"): 
      p2col1 += 1 
    elif(i[1:2] == "2"):
      p2col2 += 1 
    elif(i[1:2] == "3"):
      p2col3 += 1

    if(i == "B2"):
      middle = 2
    elif(i == "A1"):
      A1 = 2
    elif(i == "A3"):
      A3 = 2
    elif(i == "C1"):
      C1 = 2
    elif(i == "C3"):
      C3 = 2

  if(p1rowA == 3 or p1rowB == 3 or p1rowC == 3):
    print("Player 1 has won")
    return True

  elif(p1col1 == 3 or p1col2 == 3 or p1col3 == 3):
    print("Player 1 has won")
    return True

  elif(A1 == middle == C3 == 1 or C1 == middle == A3 == 1):
    print("Player 1 has won")
    return True 

  if(p2rowA == 3 or p2rowB == 3 or p2rowC == 3):
    print("Player 2 has won")
    return True

  elif(p2col1 == 3 or p2col2 == 3 or p2col3 == 3):
    print("Player 2 has won")
    return True

  elif(A1 == middle == C3 == 2 or C1 == middle == A3 == 2):
    print("Player 2 has won")
    return True 

  elif(len(moves) == 9):
    print("Draw")
    return True
    
  return False

def game():
  rounds = 0
  moves = []
  hasWon = False
  validspaces = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
  while (True):
    print("ROUND: " + str(rounds))

    if(rounds == 0):
      drawinit()
    else:
      drawgame(moves)
      
    while (True):
      p1move = input("PLAYER 1 (X): Enter Move > ")
      if (p1move in validspaces):
        moves.append("P1" + p1move)
        for i in range(len(validspaces)):
          if (validspaces[i] == p1move):
            validspaces.pop(i)
            break
            
        drawgame(moves)
        break
      else:
        print("Enter a valid position")

    hasWon = wincondition(moves)
    if(hasWon):
      break
    
    while (True):
      p2move = input("PLAYER 2 (O): Enter Move > ")
      if (p2move in validspaces):
        moves.append("P2" + p2move)
        for i in range(len(validspaces)):
          if (validspaces[i] == p2move):
            validspaces.pop(i)
            break
          
        drawgame(moves)
        break
      else:
        print("Enter a valid position")

    hasWon = wincondition(moves)
    if(hasWon):
      break
      
    rounds += 1
    print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")

  print('''
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                 Game Over
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    ''')
  
if __name__ == "__main__":
  init()
  game()
