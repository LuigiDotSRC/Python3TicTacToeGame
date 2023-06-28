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

