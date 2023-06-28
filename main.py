import tkinter as tk 
#from tkinter import ttk
import ttkbootstrap as ttk

def array_match(arrayA, arrayB): 
	result = []
	for i in arrayA: 
		if i in arrayB: 
			result.append(i)
	
	return result

def wincon(): 
	global player_move 
	global playermovelogs
	winningConditions = [
		[0,3,6],
		[1,4,7],
		[2,5,8],
		[0,1,2],
		[3,4,5],
		[6,7,8],
		[0,4,8],
		[2,4,6]
	]

	for i in winningConditions:
		matches = array_match(playermovelogs.get("X"),i)
		if len(matches) == 3: 
			return 1
	
	for i in winningConditions:
		matches = array_match(playermovelogs.get("O"),i)
		if len(matches) == 3: 
			return 2
	
	return 0
	

def capture_spot(player, button):
	global player_move
	global outputtext
	global playermovelogs

	print(player,button)
	if player == "X":
		player_color = "red"
		player_move = "O"
		outputlabel.config(text = "[O] Player 2's Move")
		
	elif player == "O":
		player_color = "blue"
		player_move = "X"
		outputlabel.config(text = "[X] Player 1's Move")

	buttons[button].config(text = player)
	buttons[button].config(state = "disabled")
	buttons[button].config(bg = player_color)
	buttons[button].config(fg = "#ffffff")
	buttons[button].config(font = "Calibri 10 bold")

	playermovelogs.get(player).append(button)
	
	if(wincon() == 1):
		for i in buttons: 
			i.config(state = "disabled")
		outputlabel.config(text = "Player 1 [X] Has Won!")
	elif(wincon() == 2):
		for i in buttons: 
			i.config(state = "disabled")
		outputlabel.config(text = "Player 2 [O] Has Won!")

# window
window = ttk.Window(themename = "darkly")
window.title("Tic Tac Toe")
window.geometry("400x500")
window.resizable(False, False)

# variables
player_move = "X"
outputtext = "[X] Player 1's Move"
playermovelogs = {"X" : [], "O" : []}


# title
title = ttk.Label(
	master=window,
	text="Tic Tac Toe",
	font="Calibri 24 bold"
)
title.grid(row=0, column=0, columnspan=3, pady=10,padx=10)

# frame
frame = tk.Frame(
	master=window
)
frame.grid(row=1, column=0, padx=15)

# buttons
buttons = []
for i in range(9):
	button = tk.Button(
		master=frame,
		text=str(i+1),
		width = 15,
		#padding = (0,30),
		height = 5,
		command = lambda index = i: capture_spot(player_move, index)
	)
	buttons.append(button)

# grid layout for buttons
for i, button in enumerate(buttons):
	button.grid(
		row=i // 3, 
		column=i % 3, 
		padx=5, 
		pady=5,
	)

# output label 
outputlabel = ttk.Label(
	master = frame,
	text = outputtext,
	font = "Calibri 12"
)
outputlabel.grid(column = 1, row = 5)

# run
window.mainloop()




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
				|		|		

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

	print("				 |		 |		 ")
	print("			" + A1 + "	|	" + A2 + "	|	" + A3)
	print("		_____|_____|_____")

	print("				 |		 |		 ")
	print("			" + B1 + "	|	" + B2 + "	|	" + B3)
	print("		_____|_____|_____")

	print("				 |		 |		 ")
	print("			" + C1 + "	|	" + C2 + "	|	" + C3)
	print("				 |		 |		 ")
	
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
	#init()
	#game()
	print()


