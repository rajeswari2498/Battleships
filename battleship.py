"""
Battleship Project
Name:
Roll No:
"""

import battleship_tests as test

project = "Battleship" # don't edit this

### SIMULATION FUNCTIONS ###

from tkinter import *
import random

EMPTY_UNCLICKED = 1
SHIP_UNCLICKED = 2
EMPTY_CLICKED = 3
SHIP_CLICKED = 4


'''
makeModel(data)
Parameters: dict mapping strs to values
Returns: None
'''
def makeModel(data):
    data["row"]= 10
    data["col"]=10
    data["boardship"]=500
    data["cellSize"] =data["boardship"]/data["row"]
    data["computerboard"] = []
    data["userboard"] =[]
    data["computerboard"]=emptyGrid(data["row"],data["col"])
    data["userboard"]=emptyGrid(data["row"],data["col"])
    data["ships"]=5
    addShips(data["computerboard"],data["ships"])
    data["temporaryShip"]=[]
    data["NumberofuserShips"]=0
    return


'''
makeView(data, userCanvas, compCanvas)
Parameters: dict mapping strs to values ; Tkinter canvas ; Tkinter canvas
Returns: None
'''
def makeView(data, userCanvas, compCanvas):
    drawGrid(data,compCanvas,data["computerboard"],True)
    drawGrid(data,userCanvas,data["userboard"],True)
    drawShip(data,userCanvas,data["temporaryShip"])
    
    return


'''
keyPressed(data, events)
Parameters: dict mapping strs to values ; key event object
Returns: None
'''
def keyPressed(data, event):
    pass


'''
mousePressed(data, event, board)
Parameters: dict mapping strs to values ; mouse event object ; 2D list of ints
Returns: None
'''
def mousePressed(data, event, board):
    outputgetclick = getClickedCell(data,event)
    if board == "user":
        clickUserBoard(data, outputgetclick[0],outputgetclick[1])
    return

#### WEEK 1 ####

'''
emptyGrid(rows, cols)
Parameters: int ; int
Returns: 2D list of ints
'''
def emptyGrid(rows, cols):
    grid = []
    for i in range(rows):
        list =[]
        for j  in range(cols):
            list.append(EMPTY_UNCLICKED)
        grid.append(list)
    return grid



'''
createShip()
Parameters: no parameters
Returns: 2D list of ints
'''
def createShip():
    row = random.randint(1,8)
    col = random.randint(1,8)
    ship = random.randint(0,1)
    if ship == 0:
        return[[row,col-1],[row,col],[row,col+1]]
    else:
        return[[row-1,col],[row,col],[row+1,col]]


'''
checkShip(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def checkShip(grid, ship):
    for each in ship:
        if grid[each[0]][each[1]] != EMPTY_UNCLICKED:
            return False
    return True


'''
addShips(grid, numShips)
Parameters: 2D list of ints ; int
Returns: 2D list of ints
'''
def addShips(grid, numShips):
    count = 0
    while count < numShips:
        ship = createShip()
        if checkShip(grid,ship) == True:
            for each in ship:
                grid[each[0]][each[1]] = SHIP_UNCLICKED
            count = count+1
    return grid


'''
drawGrid(data, canvas, grid, showShips)
Parameters: dict mapping strs to values ; Tkinter canvas ; 2D list of ints ; bool
Returns: None
'''
def drawGrid(data, canvas, grid, showShips):
    for row in range(data["row"]):
        for col in range(data["col"]):
            if grid[row][col] == SHIP_UNCLICKED:
                canvas.create_rectangle(col*data["cellSize"],row*data["cellSize"],col*data["cellSize"]+data["cellSize"],row*data["cellSize"]+data["cellSize"],fill="yellow")
            else:
                canvas.create_rectangle(col*data["cellSize"],row*data["cellSize"],col*data["cellSize"]+data["cellSize"],row*data["cellSize"]+data["cellSize"],fill="blue")



    return


### WEEK 2 ###

'''
isVertical(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isVertical(ship):
    ship.sort()
    if ship[0][1]==ship[1][1]==ship[2][1]:
        if ship[0][0]+1==ship[1][0]==ship[2][0]-1:
            return True
    return False



'''
isHorizontal(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isHorizontal(ship):
    ship.sort()
    if ship[0][0]==ship[1][0]==ship[2][0]:
        if ship[0][1]+1==ship[1][1]==ship[2][1]-1:
            return True
    return False


'''
getClickedCell(data, event)
Parameters: dict mapping strs to values ; mouse event object
Returns: list of ints
'''
def getClickedCell(data, event):
    a_coordinate = int(event.x/data["cellSize"])
    b_coordinate = int(event.y/data["cellSize"])
    return[b_coordinate,a_coordinate]


'''
drawShip(data, canvas, ship)
Parameters: dict mapping strs to values ; Tkinter canvas; 2D list of ints
Returns: None
'''
def drawShip(data, canvas, ship):
    for i in ship:
        canvas.create_rectangle(i[1]*data["cellSize"],i[0]*data["cellSize"],i[1]*data["cellSize"]+data["cellSize"],i[0]*data["cellSize"]+data["cellSize"],fill="white")


    return


'''
shipIsValid(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def shipIsValid(grid, ship):
    if checkShip(grid, ship) :
        if isVertical(ship) or isHorizontal(ship):
            return True
    return False


'''
placeShip(data)
Parameters: dict mapping strs to values
Returns: None
'''
def placeShip(data):
    if shipIsValid(data["userboard"],data["temporaryShip"]):
        for each in data["temporaryShip"]:
            data["userboard"][each[0]][each[1]] = SHIP_UNCLICKED
        data["NumberofuserShips"]+=1
    else:
        print("ship is notvalid")
    data["temporaryShip"]=[]
    return


'''
clickUserBoard(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def clickUserBoard(data, row, col):
    if data["NumberofuserShips"] == 5:
        print("Start playing the game")
        return
    if [row,col] in data["temporaryShip"]:
        return
    else:
        data["temporaryShip"].append([row,col])
    if len(data["temporaryShip"]) == 3:
        placeShip(data)


### WEEK 3 ###

'''
updateBoard(data, board, row, col, player)
Parameters: dict mapping strs to values ; 2D list of ints ; int ; int ; str
Returns: None
'''
def updateBoard(data, board, row, col, player):
    return


'''
runGameTurn(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def runGameTurn(data, row, col):
    return


'''
getComputerGuess(board)
Parameters: 2D list of ints
Returns: list of ints
'''
def getComputerGuess(board):
    return


'''
isGameOver(board)
Parameters: 2D list of ints
Returns: bool
'''
def isGameOver(board):
    return


'''
drawGameOver(data, canvas)
Parameters: dict mapping strs to values ; Tkinter canvas
Returns: None
'''
def drawGameOver(data, canvas):
    return


### SIMULATION FRAMEWORK ###

from tkinter import *

def updateView(data, userCanvas, compCanvas):
    userCanvas.delete(ALL)
    compCanvas.delete(ALL)
    makeView(data, userCanvas, compCanvas)
    userCanvas.update()
    compCanvas.update()

def keyEventHandler(data, userCanvas, compCanvas, event):
    keyPressed(data, event)
    updateView(data, userCanvas, compCanvas)

def mouseEventHandler(data, userCanvas, compCanvas, event, board):
    mousePressed(data, event, board)
    updateView(data, userCanvas, compCanvas)

def runSimulation(w, h):
    data = { }
    makeModel(data)

    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window

    # We need two canvases - one for the user, one for the computer
    Label(root, text = "USER BOARD - click cells to place ships on your board.").pack()
    userCanvas = Canvas(root, width=w, height=h)
    userCanvas.configure(bd=0, highlightthickness=0)
    userCanvas.pack()

    compWindow = Toplevel(root)
    compWindow.resizable(width=False, height=False) # prevents resizing window
    Label(compWindow, text = "COMPUTER BOARD - click to make guesses. The computer will guess on your board.").pack()
    compCanvas = Canvas(compWindow, width=w, height=h)
    compCanvas.configure(bd=0, highlightthickness=0)
    compCanvas.pack()

    makeView(data, userCanvas, compCanvas)

    root.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    compWindow.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    userCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "user"))
    compCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "comp"))

    updateView(data, userCanvas, compCanvas)

    root.mainloop()


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":
    test.testShipIsValid()

    ## Finally, run the simulation to test it manually ##
    #runSimulation(500, 500)
