"""
Battleship Project
Name:
Roll No:
"""

import battleship_tests as test

project = "Battleship" # don't edit this

### SIMULATION FUNCTIONS ###

from tkinter import *
import random as rd
#importing time
import time
#instalizing time
start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))

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
    data["rows"]=10
    data["cols"]=10
    data["board-size"]=500
    data["cell-size"]= data["board-size"]/data["rows"] #50                             #creating the cells
    data["Number of ships"]=5
    #data["user"]=emptyGrid(data["rows"], data["cols"]) 
    #User= test.testGrid()                                                           #userboard
    data["User-board"] = emptyGrid(data["rows"], data["cols"]) #test.testgrid()
    data["computer"] = emptyGrid(data["rows"], data["cols"])                        #computer board 
    #addShips(data["user"], data["Number of ships"])
    #createShip()
    addShips(data["computer"], data["Number of ships"])
    data["temp_boat"]= [] #need to kkep an []
    #print(data["temp-boat"])
    data["user_track"]=0
    data["winner"] = None
    data["max-number"] = 50
    data["current-number"] = 0
    return 

#print(makeModel())

'''
makeView(data, userCanvas, compCanvas)
Parameters: dict mapping strs to values ; Tkinter canvas ; Tkinter canvas
Returns: None
'''
def makeView(data, userCanvas, compCanvas):
    drawGrid(data, userCanvas, data["User-board"], True)
    drawShip(data, userCanvas, data["temp_boat"]) #drawship
    drawGrid(data, compCanvas, data["computer"], False)
    drawGameOver(data, userCanvas)
    return


'''
keyPressed(data, events)
Parameters: dict mapping strs to values ; key event object
Returns: None
'''
def keyPressed(data, event):
    if event:
        makeModel(data)


'''
mousePressed(data, event, board)
Parameters: dict mapping strs to values ; mouse event object ; 2D list of ints
Returns: None
'''
#uncoment the code to get run the function
def mousePressed(data, event, board):
    mouse_event = getClickedCell(data,event)   #[6,2] mouse_event[0]
    # # row = mouse_event[0]
    # # col=mouse_event[1]
    # # print(row,col)
    # # board = data["User-board"]
    # # print(mouse_event)
    # # if board == data["User-board"]:
    # #     print("user")
    # #     clickUserBoard(data, row, col)
    # #     data["User-board"]+=1
    # #     data["temp_boat"]+=1
    if data["winner"] != None:
        return
    if board == "user":
        clickUserBoard(data, mouse_event[0], mouse_event[1])
    else:
        runGameTurn(data,mouse_event[0], mouse_event[1])  #updated for project-c

    return 

#### WEEK 1 ####

'''
emptyGrid(rows, cols)
Parameters: int ; int
Returns: 2D list of ints
'''
def emptyGrid(rows, cols):
    grid=[]
    for i in range(rows):
        col = []
        for j in range(cols):
            col.append(EMPTY_UNCLICKED)
        grid.append(col)
    return (grid)


'''
createShip()
Parameters: no parameters
Returns: 2D list of ints
'''
def createShip():
    row = rd.randint(1,8)
    #print(row)
    col = rd.randint(1,8)
    #temp = [row,col]
    #print(temp)
    col_or_row = rd.randint(0,1)
    #print(col_or_row)
    ship1=[]
    
    if col_or_row == 0:                     #vertical
        for row in range(row-1, row+2):
            ship1.append([row,col])
    else:                                   #horizantal
        for col in range(col-1, col+2):
            ship1.append([row,col])
    return ship1 
    
'''
ship = [[],[],[]]
if center ==0:
    ship.append([[row-1,col],[row,col], [row+1,col]])
'''

'''
checkShip(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def checkShip(grid, ship):
    # count=0
    # for i in ship:
    #     if grid[i[0]][i[1]] == 1:
    #         count+=1
    #         if count == 3:
    #             return True
    #     else:
    #         return False
    count=[]
    for row in ship:
        #print(ship[row])
        #print(grid[row[0]][row[1]])
        if grid[row[0]][row[1]] == EMPTY_UNCLICKED:
            count.append(1)
            
            #print(count)
    return len(count) ==3 
    #return true and false
    


'''
addShips(grid, numShips)
Parameters: 2D list of ints ; int
Returns: 2D list of ints
'''
#pending
def addShips(grid, numShips):
    count=0
    #ships=[]
    while count !=  numShips:
        ship2= createShip()
        if checkShip(grid, ship2):
            for i in range(len(ship2)):
                #ships.append(SHIP_UNCLICKED) 
                grid[ship2[i][0]][ship2[i][1]] =SHIP_UNCLICKED
                
               #[[0]] [1,0]
            count+=1
    return grid



'''
drawGrid(data, canvas, grid, showShips)
Parameters: dict mapping strs to values ; Tkinter canvas ; 2D list of ints ; bool
Returns: None
'''
'''added elif statements as a part of the project-c'''
def drawGrid(data, canvas, grid, showShips):
    for row in range(data["rows"]):
        for col in range(data["cols"]):
            if grid[row][col] == SHIP_UNCLICKED:
                canvas.create_rectangle(data["cell-size"]*col, data["cell-size"]*row, data["cell-size"]*(col+1), data["cell-size"]*(row+1), fill="yellow")
            elif grid[row][col] == EMPTY_UNCLICKED:
                canvas.create_rectangle(data["cell-size"]*col, data["cell-size"]*row, data["cell-size"]*(col+1), data["cell-size"]*(row+1), fill="blue")
            elif grid[row][col] == SHIP_CLICKED:
                 canvas.create_rectangle(data["cell-size"]*col, data["cell-size"]*row, data["cell-size"]*(col+1), data["cell-size"]*(row+1), fill="red")
            elif grid[row][col] ==EMPTY_CLICKED:
                 canvas.create_rectangle(data["cell-size"]*col, data["cell-size"]*row, data["cell-size"]*(col+1), data["cell-size"]*(row+1), fill="white")
            if grid[row][col] == SHIP_UNCLICKED and showShips==False:
                canvas.create_rectangle(data["cell-size"]*col, data["cell-size"]*row, data["cell-size"]*(col+1), data["cell-size"]*(row+1), fill="blue")
           
    return


### WEEK 2 ###

'''
isVertical(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isVertical(ship):
    ship.sort()
    if ship[0][1] == ship[1][1] == ship[2][1]:
        if (ship[1][0] - ship[0][0]) and (ship[2][0]-ship[1][0]) == EMPTY_UNCLICKED:
        #print((ship[1][0] - ship[0][0]) and (ship[2][0]-ship[1][0]))
            return True
    return False
#[ [0, 1], [1, 1], [2, 1] ]
#[[0,1], [1,1], [2,1]]
'''
[0,1]-[1,1] = 1 
[2,0]-[1,0] = 1
000
100
010
111
'''
'''
isHorizontal(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isHorizontal(ship):
    ship.sort()
    if ship[0][0] == ship[2][0] and ship[1][0]==ship[2][0]:
        if (ship[0][1] == ship[1][1]-1) and (ship[2][1] == ship[1][1]+1):
            return True
    return False
#[ [1, 0], [1, 1], [1, 2] ]

'''
getClickedCell(data, event)
Parameters: dict mapping strs to values ; mouse event object
Returns: list of ints
'''
def getClickedCell(data, event):
    
    x = int(event.x/data["cell-size"])
    # print(x,type(x))
    # print(type(x))
    y= int(event.y/data["cell-size"])
    #print(type(y))
    #print(x,y)
    res = []
    res.append(y)
    res.append(x)
    #print(res)
    #res.append(x)
    return  res
#getClickedCell([12,12])

'''
drawShip(data, canvas, ship)
Parameters: dict mapping strs to values ; Tkinter canvas; 2D list of ints
Returns: None
'''
def drawShip(data, canvas, ship):
    for i in range(len(ship)):
       canvas.create_rectangle(data["cell-size"]*(ship[i][1]), data["cell-size"]*(ship[i][0]), data["cell-size"]*(ship[i][1]+1), data["cell-size"]*(ship[i][0]+1), fill="white")
    return
#[[1,3], [1.2], [3,4]]
#0 = row 1 =col [[1,1], ]

'''
shipIsValid(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def shipIsValid(grid, ship):
    #if len(ship)==3:
        if checkShip(grid, ship) and (isVertical(ship) or isHorizontal(ship)):
            return True
        return False
    


'''
placeShip(data)
Parameters: dict mapping strs to values
Returns: None
'''
def placeShip(data):
    if shipIsValid(data["User-board"], data["temp_boat"]):
        for i in data["temp_boat"]:
            data["User-board"][i[0]][i[1]] = SHIP_UNCLICKED
        data["user_track"]+=1
    else:
        print("error: ship is invalid") #syntax error
    data["temp_boat"] = []  #chaning the underscore to hiphen for document ss 
    return

#[[1,1], [3,4], [4,5]]
'''
clickUserBoard(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def clickUserBoard(data, row, col):
    if data["user_track"] == 5:         #5ships
        print("you can start the game!")
        return
    #for ship in data["temp_boat"]: #[]
        #print([row,col])
    if  [row,col] in data["temp_boat"]:
        return
    data["temp_boat"].append([row,col])
    if len(data["temp_boat"]) == 3:
        placeShip(data)
    return


### WEEK 3 ###

'''
updateBoard(data, board, row, col, player)
Parameters: dict mapping strs to values ; 2D list of ints ; int ; int ; str
Returns: None
'''
'''updated for project-c passed all testcases'''
def updateBoard(data, board, row, col, player):
    #print(row,col)
    #print(board[row][col])
    # if player == "user":
    #     board = data["computer"]
    #     #print(player)
    # else:
    #     board = data["User-board"]
        #print(player)
        
    if board[row][col] == SHIP_UNCLICKED:
        board[row][col] = SHIP_CLICKED
    else:
        if board[row][col] == EMPTY_UNCLICKED:
            board[row][col] = EMPTY_CLICKED
    if isGameOver(board):
        data["winner"] = player
    return


'''
runGameTurn(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
'''updated by shashidhar project-c'''
def runGameTurn(data, row, col):
    if data["computer"][row][col] == SHIP_CLICKED or data["computer"][row][col]==EMPTY_CLICKED:
        return
    else:
        updateBoard(data,data["computer"],row,col,"user") #completed shashidhar 
    function = getComputerGuess(data["User-board"])
    updateBoard(data,data["User-board"],function[0], function[1],"comp") #changing the argument foe doucment ss "comp"
    data["current-number"]+=1                       #within 50 moves game should complete
    if data["current-number"] == data["max-number"]:
        data["winner"] = "Draw"
    return


'''
`getComputerGuess(board)
Parameters: 2D list of ints
Returns: list of ints
'''
def getComputerGuess(board):
    row = rd.randint(0,9)
    col = rd.randint(0,9)
    #print(row,col)
    while board[row][col] == SHIP_CLICKED or board[row][col] == EMPTY_CLICKED: #assertion error 
        row = rd.randint(0,9)
        col = rd.randint(0,9)
    if board[row][col] == EMPTY_UNCLICKED or board[row][col] == SHIP_UNCLICKED:
        return [row,col]
    
'''[1,0]
[2,0]
'''
    


'''
isGameOver(board)
Parameters: 2D list of ints
Returns: bool
'''
def isGameOver(board):
    for row in range(len(board)):
        for j in range(len(board[row])):
            if board[row][j] == SHIP_UNCLICKED:
                return False
    return True
   


'''
drawGameOver(data, canvas)
Parameters: dict mapping strs to values ; Tkinter canvas
Returns: None
'''
def drawGameOver(data, canvas):
    if data["winner"] == "user":
        canvas.create_text(250, 50, text="You are winner!", fill="black", font=('Helvetica 30 bold'))
        canvas.create_text(250, 100, text="Press enter to play again", fill="black", font=('Helvetica 20 bold'))
    elif data["winner"] == "comp":
        canvas.create_text(250, 50, text="You lost!", fill="black",  font=('Helvetica 30 bold') )
        canvas.create_text(250, 100, text="Press enter to play again", fill="black", font=('Helvetica 20 bold'))
    elif data["winner"] == "Draw":
        canvas.create_text(250, 50, text="It's a Draw", fill="black",  font=('Helvetica 30 bold') )
        canvas.create_text(250, 100, text="Press enter to play again", fill="black", font=('Helvetica 20 bold'))
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

def mouseEventHandler(data, userCanvas, compCanvas, event, board,):
    mousePressed(data, event, board)
    updateView(data, userCanvas, compCanvas)

def runSimulation(w, h):
    data = { }
    #getClickedCell()
    makeModel(data)
    #print(data)

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

    ## Finally, run the simulation to test it manually ##
    runSimulation(500, 500)
    #test.testIsHorizontal()
    #test.testIsVertical()
    #test.testUpdateBoard()
    #test.testGetComputerGuess()
    #test.testIsGameOver()
