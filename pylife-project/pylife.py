#pylife.py
#Cpts 481 Python Software
#Professor Robert Lewis
#Student Anita Whyatt
#Homework #6



cellArray = [
	[ (0,0), "dead" ],
	[ (1,0), "dead" ],
	[ (2,0), "dead" ],
	[ (3,0), "dead" ],
	[ (4,0), "dead" ],
	[ (5,0), "dead" ],
	[ (6,0), "dead" ],
	[ (7,0), "dead" ],
	[ (8,0), "dead" ],
	[ (9,0), "dead" ],
	[ (10,0), "dead" ],
	[ (11,0), "dead" ],
	[ (12,0), "dead" ],
	[ (13,0), "dead" ],
	[ (14,0), "dead" ],
	[ (15,0), "dead" ],
	[ (16,0), "dead" ],
	[ (17,0), "dead" ],
	[ (18,0), "dead" ],
	[ (19,0), "dead" ],
	#[ (20,0), "dead" ],
	[ (0,1), "dead" ],
	[ (1,1), "dead" ],
	[ (2,1), "dead" ],
	[ (3,1), "dead" ],
	[ (4,1), "dead" ],
	[ (5,1), "dead" ],
	[ (6,1), "dead" ],
	[ (7,1), "dead" ],
	[ (8,1), "dead" ],
	[ (9,1), "dead" ],
	[ (10,1), "dead" ],
	[ (11,1), "dead" ],
	[ (12,1), "dead" ],
	[ (13,1), "dead" ],
	[ (14,1), "dead" ],
	[ (15,1), "dead" ],
	[ (16,1), "dead" ],
	[ (17,1), "dead" ],
	[ (18,1), "dead" ],
	[ (19,1), "dead" ],
	#[ (20,1), "dead" ],
	[ (0,2), "dead" ],
	[ (1,2), "dead" ],
	[ (2,2), "dead" ],
	[ (3,2), "dead" ],
	[ (4,2), "dead" ],
	[ (5,2), "dead" ],
	[ (6,2), "dead" ],
	[ (7,2), "dead" ],
	[ (8,2), "dead" ],
	[ (9,2), "dead" ],
	[ (10,2), "dead" ],
	[ (11,2), "dead" ],
	[ (12,2), "dead" ],
	[ (13,2), "dead" ],
	[ (14,2), "dead" ],
	[ (15,2), "dead" ],
	[ (16,2), "dead" ],
	[ (17,2), "dead" ],
	[ (18,2), "dead" ],
	[ (19,2), "dead" ],
	#[ (20,2), "dead" ],
	[ (0,3), "dead" ],
	[ (1,3), "dead" ],
	[ (2,3), "dead" ],
	[ (3,3), "dead" ],
	[ (4,3), "dead" ],
	[ (5,3), "dead" ],
	[ (6,3), "dead" ],
	[ (7,3), "dead" ],
	[ (8,3), "dead" ],
	[ (9,3), "dead" ],
	[ (10,3), "dead" ],
	[ (11,3), "dead" ],
	[ (12,3), "dead" ],
	[ (13,3), "dead" ],
	[ (14,3), "dead" ],
	[ (15,3), "dead" ],
	[ (16,3), "dead" ],
	[ (17,3), "dead" ],
	[ (18,3), "dead" ],
	[ (19,3), "dead" ],
	#[ (20,3), "dead" ],
	[ (0,4), "dead" ],
	[ (1,4), "dead" ],
	[ (2,4), "dead" ],
	[ (3,4), "dead" ],
	[ (4,4), "dead" ],
	[ (5,4), "dead" ],
	[ (6,4), "dead" ],
	[ (7,4), "dead" ],
	[ (8,4), "dead" ],
	[ (9,4), "dead" ],
	[ (10,4), "dead" ],
	[ (11,4), "dead" ],
	[ (12,4), "dead" ],
	[ (13,4), "dead" ],
	[ (14,4), "dead" ],
	[ (15,4), "dead" ],
	[ (16,4), "dead" ],
	[ (17,4), "dead" ],
	[ (18,4), "dead" ],
	[ (19,4), "dead" ],
	#[ (20,4), "dead" ],
	[ (0,5), "dead" ],
	[ (1,5), "dead" ],
	[ (2,5), "dead" ],
	[ (3,5), "dead" ],
	[ (4,5), "dead" ],
	[ (5,5), "dead" ],
	[ (6,5), "dead" ],
	[ (7,5), "dead" ],
	[ (8,5), "dead" ],
	[ (9,5), "dead" ],
	[ (10,5), "dead" ],
	[ (11,5), "dead" ],
	[ (12,5), "dead" ],
	[ (13,5), "dead" ],
	[ (14,5), "dead" ],
	[ (15,5), "dead" ],
	[ (16,5), "dead" ],
	[ (17,5), "dead" ],
	[ (18,5), "dead" ],
	[ (19,5), "dead" ],
	#[ (20,5), "dead" ],
	[ (0,6), "dead" ],
	[ (1,6), "dead" ],
	[ (2,6), "dead" ],
	[ (3,6), "dead" ],
	[ (4,6), "dead" ],
	[ (5,6), "dead" ],
	[ (6,6), "dead" ],
	[ (7,6), "dead" ],
	[ (8,6), "dead" ],
	[ (9,6), "dead" ],
	[ (10,6), "dead" ],
	[ (11,6), "dead" ],
	[ (12,6), "dead" ],
	[ (13,6), "dead" ],
	[ (14,6), "dead" ],
	[ (15,6), "dead" ],
	[ (16,6), "dead" ],
	[ (17,6), "dead" ],
	[ (18,6), "dead" ],
	[ (19,6), "dead" ],
	#[ (20,6), "dead" ],
	[ (0,7), "dead" ],
	[ (1,7), "dead" ],
	[ (2,7), "dead" ],
	[ (3,7), "dead" ],
	[ (4,7), "dead" ],
	[ (5,7), "dead" ],
	[ (6,7), "dead" ],
	[ (7,7), "dead" ],
	[ (8,7), "dead" ],
	[ (9,7), "dead" ],
	[ (10,7), "dead" ],
	[ (11,7), "dead" ],
	[ (12,7), "dead" ],
	[ (13,7), "dead" ],
	[ (14,7), "dead" ],
	[ (15,7), "dead" ],
	[ (16,7), "dead" ],
	[ (17,7), "dead" ],
	[ (18,7), "dead" ],
	[ (19,7), "dead" ],
	#[ (20,7), "dead" ],
	[ (0,8), "dead" ],
	[ (1,8), "dead" ],
	[ (2,8), "dead" ],
	[ (3,8), "dead" ],
	[ (4,8), "dead" ],
	[ (5,8), "dead" ],
	[ (6,8), "dead" ],
	[ (7,8), "dead" ],
	[ (8,8), "dead" ],
	[ (9,8), "dead" ],
	[ (10,8), "dead" ],
	[ (11,8), "dead" ],
	[ (12,8), "dead" ],
	[ (13,8), "dead" ],
	[ (14,8), "dead" ],
	[ (15,8), "dead" ],
	[ (16,8), "dead" ],
	[ (17,8), "dead" ],
	[ (18,8), "dead" ],
	[ (19,8), "dead" ],
	#[ (20,8), "dead" ],
	[ (0,9), "dead" ],
	[ (1,9), "dead" ],
	[ (2,9), "dead" ],
	[ (3,9), "dead" ],
	[ (4,9), "dead" ],
	[ (5,9), "dead" ],
	[ (6,9), "dead" ],
	[ (7,9), "dead" ],
	[ (8,9), "dead" ],
	[ (9,9), "dead" ],
	[ (10,9), "dead" ],
	[ (11,9), "dead" ],
	[ (12,9), "dead" ],
	[ (13,9), "dead" ],
	[ (14,9), "dead" ],
	[ (15,9), "dead" ],
	[ (16,9), "dead" ],
	[ (17,9), "dead" ],
	[ (18,9), "dead" ],
	[ (19,9), "dead" ],
	#[ (20,9), "dead" ],
	[ (0,10), "dead" ],
	[ (1,10), "dead" ],
	[ (2,10), "dead" ],
	[ (3,10), "dead" ],
	[ (4,10), "dead" ],
	[ (5,10), "dead" ],
	[ (6,10), "dead" ],
	[ (7,10), "dead" ],
	[ (8,10), "dead" ],
	[ (9,10), "dead" ],
	[ (10,10), "dead" ],
	[ (11,10), "dead" ],
	[ (12,10), "dead" ],
	[ (13,10), "dead" ],
	[ (14,10), "dead" ],
	[ (15,10), "dead" ],
	[ (16,10), "dead" ],
	[ (17,10), "dead" ],
	[ (18,10), "dead" ],
	[ (19,10), "dead" ],
	#[ (20,10), "dead" ],
	[ (0,11), "dead" ],
	[ (1,11), "dead" ],
	[ (2,11), "dead" ],
	[ (3,11), "dead" ],
	[ (4,11), "dead" ],
	[ (5,11), "dead" ],
	[ (6,11), "dead" ],
	[ (7,11), "dead" ],
	[ (8,11), "dead" ],
	[ (9,11), "dead" ],
	[ (10,11), "dead" ],
	[ (11,11), "dead" ],
	[ (12,11), "dead" ],
	[ (13,11), "dead" ],
	[ (14,11), "dead" ],
	[ (15,11), "dead" ],
	[ (16,11), "dead" ],
	[ (17,11), "dead" ],
	[ (18,11), "dead" ],
	[ (19,11), "dead" ],
	#[ (20,11), "dead" ],
	[ (0,12), "dead" ],
	[ (1,12), "dead" ],
	[ (2,12), "dead" ],
	[ (3,12), "dead" ],
	[ (4,12), "dead" ],
	[ (5,12), "dead" ],
	[ (6,12), "dead" ],
	[ (7,12), "dead" ],
	[ (8,12), "dead" ],
	[ (9,12), "dead" ],
	[ (10,12), "dead" ],
	[ (11,12), "dead" ],
	[ (12,12), "dead" ],
	[ (13,12), "dead" ],
	[ (14,12), "dead" ],
	[ (15,12), "dead" ],
	[ (16,12), "dead" ],
	[ (17,12), "dead" ],
	[ (18,12), "dead" ],
	[ (19,12), "dead" ],
	#[ (20,12), "dead" ],
	[ (0,13), "dead" ],
	[ (1,13), "dead" ],
	[ (2,13), "dead" ],
	[ (3,13), "dead" ],
	[ (4,13), "dead" ],
	[ (5,13), "dead" ],
	[ (6,13), "dead" ],
	[ (7,13), "dead" ],
	[ (8,13), "dead" ],
	[ (9,13), "dead" ],
	[ (10,13), "dead" ],
	[ (11,13), "dead" ],
	[ (12,13), "dead" ],
	[ (13,13), "dead" ],
	[ (14,13), "dead" ],
	[ (15,13), "dead" ],
	[ (16,13), "dead" ],
	[ (17,13), "dead" ],
	[ (18,13), "dead" ],
	[ (19,13), "dead" ],
	#[ (20,13), "dead" ],
	[ (0,14), "dead" ],
	[ (1,14), "dead" ],
	[ (2,14), "dead" ],
	[ (3,14), "dead" ],
	[ (4,14), "dead" ],
	[ (5,14), "dead" ],
	[ (6,14), "dead" ],
	[ (7,14), "dead" ],
	[ (8,14), "dead" ],
	[ (9,14), "dead" ],
	[ (10,14), "dead" ],
	[ (11,14), "dead" ],
	[ (12,14), "dead" ],
	[ (13,14), "dead" ],
	[ (14,14), "dead" ],
	[ (15,14), "dead" ],
	[ (16,14), "dead" ],
	[ (17,14), "dead" ],
	[ (18,14), "dead" ],
	[ (19,14), "dead" ],
	#[ (20,14), "dead" ],
	[ (0,15), "dead" ],
	[ (1,15), "dead" ],
	[ (2,15), "dead" ],
	[ (3,15), "dead" ],
	[ (4,15), "dead" ],
	[ (5,15), "dead" ],
	[ (6,15), "dead" ],
	[ (7,15), "dead" ],
	[ (8,15), "dead" ],
	[ (9,15), "dead" ],
	[ (10,15), "dead" ],
	[ (11,15), "dead" ],
	[ (12,15), "dead" ],
	[ (13,15), "dead" ],
	[ (14,15), "dead" ],
	[ (15,15), "dead" ],
	[ (16,15), "dead" ],
	[ (17,15), "dead" ],
	[ (18,15), "dead" ],
	[ (19,15), "dead" ],
	#[ (20,15), "dead" ],
	[ (0,16), "dead" ],
	[ (1,16), "dead" ],
	[ (2,16), "dead" ],
	[ (3,16), "dead" ],
	[ (4,16), "dead" ],
	[ (5,16), "dead" ],
	[ (6,16), "dead" ],
	[ (7,16), "dead" ],
	[ (8,16), "dead" ],
	[ (9,16), "dead" ],
	[ (10,16), "dead" ],
	[ (11,16), "dead" ],
	[ (12,16), "dead" ],
	[ (13,16), "dead" ],
	[ (14,16), "dead" ],
	[ (15,16), "dead" ],
	[ (16,16), "dead" ],
	[ (17,16), "dead" ],
	[ (18,16), "dead" ],
	[ (19,16), "dead" ],
	#[ (20,16), "dead" ],
	[ (0,17), "dead" ],
	[ (1,17), "dead" ],
	[ (2,17), "dead" ],
	[ (3,17), "dead" ],
	[ (4,17), "dead" ],
	[ (5,17), "dead" ],
	[ (6,17), "dead" ],
	[ (7,17), "dead" ],
	[ (8,17), "dead" ],
	[ (9,17), "dead" ],
	[ (10,17), "dead" ],
	[ (11,17), "dead" ],
	[ (12,17), "dead" ],
	[ (13,17), "dead" ],
	[ (14,17), "dead" ],
	[ (15,17), "dead" ],
	[ (16,17), "dead" ],
	[ (17,17), "dead" ],
	[ (18,17), "dead" ],
	[ (19,17), "dead" ],
	#[ (20,17), "dead" ],
	[ (0,18), "dead" ],
	[ (1,18), "dead" ],
	[ (2,18), "dead" ],
	[ (3,18), "dead" ],
	[ (4,18), "dead" ],
	[ (5,18), "dead" ],
	[ (6,18), "dead" ],
	[ (7,18), "dead" ],
	[ (8,18), "dead" ],
	[ (9,18), "dead" ],
	[ (10,18), "dead" ],
	[ (11,18), "dead" ],
	[ (12,18), "dead" ],
	[ (13,18), "dead" ],
	[ (14,18), "dead" ],
	[ (15,18), "dead" ],
	[ (16,18), "dead" ],
	[ (17,18), "dead" ],
	[ (18,18), "dead" ],
	[ (19,18), "dead" ],
	#[ (20,18), "dead" ],
	[ (0,19), "dead" ],
	[ (1,19), "dead" ],
	[ (2,19), "dead" ],
	[ (3,19), "dead" ],
	[ (4,19), "dead" ],
	[ (5,19), "dead" ],
	[ (6,19), "dead" ],
	[ (7,19), "dead" ],
	[ (8,19), "dead" ],
	[ (9,19), "dead" ],
	[ (10,19), "dead" ],
	[ (11,19), "dead" ],
	[ (12,19), "dead" ],
	[ (13,19), "dead" ],
	[ (14,19), "dead" ],
	[ (15,19), "dead" ],
	[ (16,19), "dead" ],
	[ (17,19), "dead" ],
	[ (18,19), "dead" ],
	[ (19,19), "dead" ],
	#[ (20,19), "dead" ],
]


from tkinter import *

root = Tk()
root.title("The Game Of Life")

runIsGo = False

################
#Functions Here:
################
def quitEvent():
	root.destroy()

def clearEvent():
	for item in cellArray:
		item[1] = "dead"
	canvasBoard.create_rectangle(0, 0, 410, 410, outline="white", fill="white")

def whiteCell(coordinates): #takes cell coordinates and "whites" out cell
	baseX = int(20 * coordinates[0])
	baseY = int(20 * coordinates[1])
	canvasBoard.create_rectangle(baseX, baseY, baseX+20, baseY+20, outline="white", fill="white")
	
def blackCell(coordinates): #takes cell coordinates and "blacks" cell
	baseX = int(20 * coordinates[0])
	baseY = int(20 * coordinates[1])
	canvasBoard.create_rectangle(baseX, baseY, baseX+20, baseY+20, outline="black", fill="black")

	

def clickEvent(event): #if the user clicks somewhere on the canvas
	x = event.x
	y = event.y
	moduloX = x % 20
	moduloY = y % 20
	baseX = x - moduloX
	baseY = y - moduloY
	coordinateX = int(baseX / 20)
	coordinateY = int(baseY / 20)
	coordinates = (coordinateX, coordinateY)
	#print("Coordinates are: ", coordinates)
	#Update our list dead/alive status, and canvas colors:
	for item in cellArray:
		if item[0] == coordinates:
			if item[1] == "dead":
				item[1] = "alive"
				canvasBoard.create_rectangle(baseX, baseY, baseX+20, baseY+20, outline="black", fill="black")
			elif item[1] == "alive":
				item[1] = "dead"
				canvasBoard.create_rectangle(baseX, baseY, baseX+20, baseY+20, outline="white", fill="white")


def getNeighbors(cell): #takes cell coordinates returns all existing neighbor coordinates
	allNeighbors = [] #list will store all neighbors
	liveNeighbors = [] #will store live neighbors
	#Upper left test and add
	if cell[0]-1 >= 0 and cell[1]-1 >= 0:
		allNeighbors.append( (cell[0]-1, cell[1]-1) )
	#Upper middle test and add
	if cell[1]-1 >= 0:
		allNeighbors.append( (cell[0], cell[1]-1) )
	#Upper right test and add
	if cell[0]+1 <= 19 and cell[1]-1 >= 0:
		allNeighbors.append( (cell[0]+1, cell[1]-1) )
	#Middle right test and add
	if cell[0]+1 <= 19:
		allNeighbors.append( (cell[0]+1, cell[1]) )
	#Bottom right test and add
	if cell[0]+1 <= 19 and cell[1]+1 <= 19:
		allNeighbors.append( (cell[0]+1, cell[1]+1) )
	#Bottom middle test and add
	if cell[1]+1 <= 19:
		allNeighbors.append( (cell[0], cell[1]+1) )
	#Bottom middle test and add
	if cell[0]-1 >= 0 and cell[1]+1 <= 19:
		allNeighbors.append( (cell[0]-1, cell[1]+1) )
	#Middle left test and add
	if cell[0]-1 >= 0:
		allNeighbors.append( (cell[0]-1, cell[1]) )
	
	for neighCell in allNeighbors:
		for cell in cellArray:
			if neighCell == cell[0]:
				if cell[1] == "alive":
					liveNeighbors.append(neighCell)
	
	return(liveNeighbors)
	



def stepEvent():
	newCellArray = [] #will hold updated cellArray
	global cellArray
	for cell in cellArray:
		#cell = cellArray[21]
		#print("\nOur cell: ", cell)
		livingN = getNeighbors(cell[0])
		#print("live: ", livingN)
		if cell[1] == "dead":
			if len(livingN) == 3:
				newCellArray.append( [cell[0], "alive"] )
				blackCell(cell[0])
		elif cell[1] == "alive":
			if len(livingN) < 2 or len(livingN) > 3:
				newCellArray.append( [cell[0], "dead"] )
				whiteCell(cell[0])
		else:
			newCellArray.append( [cell[0], cell[1]] )
	
	#print("Current new cell list: ", newCellArray)
	cellArray = newCellArray	
	
def toggleRun():
	global runIsGo
	if runIsGo == True:
		globals()['runIsGo'] = False
	elif runIsGo == False:
		globals()['runIsGo'] = True
	
	
def runEvent():
	global runIsGo
	root.after(1000, runEvent)
	if runIsGo == True:
		stepEvent()
	


#######################
#Canvas Structure Here:
#######################

canvasBoard = Canvas(root, width=400, height=400, bg="white")
canvasBoard.bind("<Button-1>", clickEvent)
canvasBoard.pack()

runFrame = Frame(root, relief=RAISED, borderwidth=1)
runBtn = Button(master=runFrame, width=8, height=2, font=("Courier", 14), text="Run", command=toggleRun)
runBtn.pack()
runFrame.pack(side=RIGHT)

quitFrame = Frame(root, relief=RAISED, borderwidth=1)
quitBtn = Button(master=quitFrame, width=8, height=2, font=("Courier", 14), text="Quit", command=quitEvent)
quitBtn.pack()
quitFrame.pack(side=RIGHT)

clearFrame = Frame(root, relief=RAISED, borderwidth=1)
clearBtn = Button(master=clearFrame, width=8, height=2, font=("Courier", 14), text="Clear", command=clearEvent)
clearBtn.pack()
clearFrame.pack(side=RIGHT)

stepFrame = Frame(root, relief=RAISED, borderwidth=1)
stepBtn = Button(master=stepFrame, width=8, height=2, font=("Courier", 14), text="Step", command=stepEvent)
stepBtn.pack()
stepFrame.pack(side=RIGHT)

runEvent()




#mainloop somewhere at bottom
root.mainloop()























