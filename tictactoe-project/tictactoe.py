#tictactoe.py
#Homework #5
#Cpts 481 Python Software
#Professor Robert Lewis
#Anita Whyatt

import tkinter as tk

from functools import partial

import random


####################################
#######Function Declared Here#######
####################################
#some global variables
gameStillOn = True
lastOMove = ""
moveCount = 1

#invoked by quit button, quits the application
def quitFunc():
	window.destroy()

#decides what to do if user pushes button.  Should nothing happen?
#or should the button's text change, and player x takes their turn?
def buttonPushedWhatDo(button):
	textInButton = ""
	if button == "tl":
		textInButton = btn_tl['text']
	elif button == "t":
		textInButton = btn_t['text']
	elif button == "tr":
		textInButton = btn_tr['text']
	elif button == "l":
		textInButton = btn_l['text']
	elif button == 'm':
		textInButton = btn_m['text']
	elif button == 'r':
		textInButton = btn_r['text']
	elif button == 'bl':
		textInButton = btn_bl['text']
	elif button == 'b':
		textInButton = btn_b['text']
	elif button == 'br':
		textInButton = btn_br['text']
	
	if textInButton != " ":
		print("Invalide tile, please choose again!")
	else:
		global lastOMove #works for the entirity of the if/elif loops
		if button == "tl" and gameStillOn==True:
			btn_tl['text'] = "O"
			lastOMove = "tl"
		elif button == "t" and gameStillOn==True:
			btn_t['text'] = "O"
			lastOMove = "t"
		elif button == "tr" and gameStillOn==True:
			btn_tr['text'] = "O"
			lastOMove = "tr"
		elif button == "l" and gameStillOn==True:
			btn_l['text'] = "O"
			lastOMove = "l"
		elif button == 'm' and gameStillOn==True:
			btn_m['text'] = "O"
			lastOMove = "m"
		elif button == 'r' and gameStillOn==True:
			btn_r['text'] = "O"
			lastOMove = "r"
		elif button == 'bl' and gameStillOn==True:
			btn_bl['text'] = "O"
			lastOMove = "bl"
		elif button == 'b' and gameStillOn==True:
			btn_b['text'] = "O"
			lastOMove = "b"
		elif button == 'br' and gameStillOn==True:
			btn_br['text'] = "O"
			lastOMove = "br"
		#Finally check if game is still on and call player X's turn
		isGameStillOn()
		playerXTurn()
		



#Check is the board in a win condition or a cat's game
def isGameStillOn():
	tl_text = btn_tl['text']
	t_text = btn_t['text']
	tr_text = btn_tr['text']
	l_text = btn_l['text']
	m_text = btn_m['text']
	r_text = btn_r['text']
	bl_text = btn_bl['text']
	b_text = btn_b['text']
	br_text = btn_br['text']
	#now we check to see if it is a cat's game
	if tl_text != " " and t_text != " " and tr_text != " " and l_text != " " and m_text != " " and r_text != " " and bl_text != " " and b_text != " " and br_text != " ":
		output_label['text'] = "Cat's Game"
	#these will update the label if a win condition has been reached
	threeInARow(tl_text, t_text, tr_text)
	threeInARow(l_text, m_text, r_text)
	threeInARow(bl_text, b_text, br_text)
	threeInARow(tl_text, l_text, bl_text)
	threeInARow(t_text, m_text, b_text)
	threeInARow(tr_text, r_text, br_text)
	threeInARow(tl_text, m_text, br_text)
	threeInARow(tr_text, m_text, bl_text)
	if output_label['text'] != "Your Turn!":
		global gameStillOn 
		gameStillOn = False
	
	

#helper function for isGameStillOn
def threeInARow(b1, b2, b3):
	#print("threeInARow called: ", b1, b2, b3)
	if b1 == "X" and b1 == b2 and b2 == b3:
		output_label['text'] = "X Wins!"
	elif b1 == "O" and b1 == b2 and b2 == b3:
		output_label['text'] = "O Wins!"


	

#Player X takes their turn, where should he move?
def playerXTurn():
	global moveCount
	print("Player X takes their turn!")
	print("Last O Move was: ", lastOMove)
	print("Move Count: ", moveCount)
	needRandomSelection = False
	
	
	if moveCount == 1: #first move
		if lastOMove == "tl":
			btn_t['text'] = "X"
		elif lastOMove == "t":
			btn_tr['text'] = "X"
		elif lastOMove == "tr":
			btn_r['text'] = "X"
		elif lastOMove == "l":
			btn_tl['text'] = "X"
		elif lastOMove == 'r':
			btn_br['text'] = "X"
		elif lastOMove == 'bl':
			btn_l['text'] = "X"
		elif lastOMove == 'b':
			btn_bl['text'] = "X"
		elif lastOMove == 'br':
			btn_b['text'] = "X"
		moveCount += 2 #increment by two for both O and X taking their turns
	elif moveCount != 1 and gameStillOn == True:
		if lastOMove == "tl":
			if btn_br['text'] == " ":
				btn_br['text'] = "X"
			elif btn_t['text'] == " ":
				btn_t['text'] = "X"
			else:
				needRandomSelection = True
		elif lastOMove == "t":
			if btn_b['text'] == " ":
				btn_b['text'] = "X"
			elif btn_tr['text'] == " ":
				btn_tr['text'] = "X"
			else:
				needRandomSelection = True
		elif lastOMove == "tr":
			if btn_bl['text'] == " ":
				btn_bl['text'] = "X"
			elif btn_r['text'] == " ":
				btn_r['text'] = "X"
			else:
				needRandomSelection = True
		elif lastOMove == "l":
			if btn_r['text'] == " ":
				btn_r['text'] = "X"
			elif btn_tl['text'] == " ":
				btn_tl['text'] = "X"
			else:
				needRandomSelection = True
		elif lastOMove == 'r':
			if btn_l['text'] == " ":
				btn_l['text'] = "X"
			elif btn_br['text'] == " ":
				btn_br['text'] = "X"
			else:
				needRandomSelection = True
		elif lastOMove == 'bl':
			if btn_tr['text'] == " ":
				btn_tr['text'] = "X"
			elif btn_l['text'] == " ":
				btn_l['text'] = "X"
			else:
				needRandomSelection = True
		elif lastOMove == 'b':
			if btn_t['text'] == " ":
				btn_t['text'] = "X"
			elif btn_bl['text'] == " ":
				btn_bl['text'] = "X"
			else:
				needRandomSelection = True
		elif lastOMove == 'br':
			if btn_tl['text'] == " ":
				btn_tl['text'] = "X"
			elif btn_b['text'] == " ":
				btn_b['text'] = "X"
			else:
				needRandomSelection = True
		moveCount += 2
		#check if game still on
		isGameStillOn()
		if needRandomSelection == True and gameStillOn == True:
			randomMove()
		
#helper function for playerXTurn
def randomMove():
	print("randomMove invoke")
	listOfBlankTiles = [] #empty list
	randTile = ""
	if btn_tl['text'] == " ":
		listOfBlankTiles.append("tl")
	if btn_t['text'] == " ":
		listOfBlankTiles.append("t")
	if btn_tr['text'] == " ":
		listOfBlankTiles.append("tr")
	if btn_l['text'] == " ":
		listOfBlankTiles.append("l")
	if btn_m['text'] == " ":
		listOfBlankTiles.append("m")
	if btn_r['text'] == " ":
		listOfBlankTiles.append("r")
	if btn_bl['text'] == " ":
		listOfBlankTiles.append("bl")
	if btn_b['text'] == " ":
		listOfBlankTiles.append("b")
	if btn_br['text'] == " ":
		listOfBlankTiles.append("br")
	if listOfBlankTiles != []:
		randTile = random.choice(listOfBlankTiles)
		if randTile == "tl":
			btn_tl['text'] = "X"
		if randTile == "t":
			btn_t['text'] = "X"
		if randTile == "tr":
			btn_tr['text'] = "X"
		if randTile == "l":
			btn_l['text'] = "X"
		if randTile == "m":
			btn_m['text'] = "X"
		if randTile == "r":
			btn_r['text'] = "X"
		if randTile == "bl":
			btn_bl['text'] = "X"
		if randTile == "b":
			btn_b['text'] = "X"
		if randTile == "br":
			btn_br['text'] = "X"
	#check if gameStillOn
	isGameStillOn()
			
		
	



########################################
#######Define Window Details Here#######
########################################
window = tk.Tk()
window.title("Tic Tac Toe")
window.resizable(width=False, height=False)
window.rowconfigure([0, 1, 2, 3], minsize=100)
window.columnconfigure([0, 1, 2], minsize=100)
#TOP LEFT BUTTON
frame_tl = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame_tl.grid(row=0, column=0, padx=5, pady=5)
btn_tl = tk.Button(master=frame_tl, width=4, height=2, font=("Courier", 44), text=" ", command=partial(buttonPushedWhatDo, "tl"))
btn_tl.pack()
#TOP MIDDLE BUTTON
frame_t = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame_t.grid(row=0, column=1, padx=5, pady=5)
btn_t = tk.Button(master=frame_t, width=4, height=2, font=("Courier", 44), text=" ", command=partial(buttonPushedWhatDo, "t"))
btn_t.pack()
#TOP RIGHT BUTTON 
frame_tr = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame_tr.grid(row=0, column=2, padx=5, pady=5)
btn_tr = tk.Button(master=frame_tr, width=4, height=2, font=("Courier", 44), text=" ", command=partial(buttonPushedWhatDo, "tr"))
btn_tr.pack()
#LEFT MIDDLE BUTTON
frame_l = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame_l.grid(row=1, column=0, padx=5, pady=5)
btn_l = tk.Button(master=frame_l, width=4, height=2, font=("Courier", 44), text=" ", command=partial(buttonPushedWhatDo, "l"))
btn_l.pack()
#MIDDLE MOST BUTTON
frame_m = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame_m.grid(row=1, column=1, padx=5, pady=5)
btn_m = tk.Button(master=frame_m, width=4, height=2, font=("Courier", 44), text="X", command=partial(buttonPushedWhatDo, "m"))
btn_m.pack()
#RIGHT MIDDLE BUTTON
frame_r = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame_r.grid(row=1, column=2, padx=5, pady=5)
btn_r = tk.Button(master=frame_r, width=4, height=2, font=("Courier", 44), text=" ", command=partial(buttonPushedWhatDo, "r"))
btn_r.pack()
#BOTTOM LEFT BUTTON
frame_bl = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame_bl.grid(row=2, column=0, padx=5, pady=5)
btn_bl = tk.Button(master=frame_bl, width=4, height=2, font=("Courier", 44), text=" ", command=partial(buttonPushedWhatDo, "bl"))
btn_bl.pack()
#BOTTOM MIDDLE BUTTON
frame_b = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame_b.grid(row=2, column=1, padx=5, pady=5)
btn_b = tk.Button(master=frame_b, width=4, height=2, font=("Courier", 44), text=" ", command=partial(buttonPushedWhatDo, "b"))
btn_b.pack()
#BOTTOM RIGHT BUTTON
frame_br = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame_br.grid(row=2, column=2, padx=5, pady=5)
btn_br = tk.Button(master=frame_br, width=4, height=2, font=("Courier", 44), text=" ", command=partial(buttonPushedWhatDo, "br") )
btn_br.pack()
#OUTPUT LABEL
frame_output_label = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame_output_label.grid(row=3, column=0, padx=5, pady=5)
output_label = tk.Label(master=frame_output_label, width=10, height=2, font=("Courier", 12), text="Your Turn!")
output_label.pack()
#QUIT BUTTON
frame_quit_button = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame_quit_button.grid(row=3, column=2, padx=5, pady=5)
quit_button = tk.Button(master=frame_quit_button, width=5, height=2, font=("Courier", 12), text="Quit", command=quitFunc)
quit_button.pack()



#######Action Phase Somewhere Down Here#######
	#Maybe?




#main loop somewhere at bottom
window.mainloop()





























































































