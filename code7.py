gameBoard = [ ["X", " ", "O"], [" ", "X", " "], [" ", " ", "O"] ]
#We have given varible called gameBoard and we have given the list of the rows and columns
for row in range(len(gameBoard)): # each row is a list
    boardString = ""#We have assigned an empty string by using a variable boardString.
    for col in range(len(gameBoard[row])): # each col is a string
        boardString = boardString + gameBoard[row][col]
        #We are adding the empty string and the gameboard variable  with the index of its rows and columns
    print(boardString) # separate rows on separate lines