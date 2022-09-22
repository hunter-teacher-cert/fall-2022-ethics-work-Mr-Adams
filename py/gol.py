# FILENAME cgol.py
# First Last Seth Adams
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: previous work from summer

import random

def createNewBoard (rows, cols):
  board = [["." for c in range(cols)]for r in range(rows)]
  return board

def printBoard(board):
  for r in range(len(board)):
    for c in range(len(board[r])):
      print(board[r][c], end = " ")
      
  print( )
     
def setCell(board, r, c, val):
  board [r][c] = val

def countNeighbours(board, row, col):
  count = 0 #intialize
  for r in range(row-1, row + 2):
    if r < 0: #if r cycles above top row
      continue
    if r >= len(board): #bottom boundary
      break
    for c in range(col-1, col + 2):
      if c < 0: #left boundary
        continue
      if c >= len(board[0]): #right boundary
        break
        
      #don't count the actual middle cell
      if not(r == row and c == col):

        #check if the cell is alive
        if board[r][c] == 'X':

          #increment the count
          count = count + 1
  return count

def getNextGenCell(board,r,c):
  nextGen = board[r][c] #target cell as indicated in the main
  count = countNeighbours(board, r, c)
  
  #check if alive
  isAlive = False
  if board[r][c] == 'X':
    isAlive = True

#Every cell with <2 neighbours will die from isolation.
  if isAlive and count<2:
    nextGen = '.'
#Each cell with >3 neighbours will die from overpopulation.
  if isAlive and count>3:
    nextGen = '.'

  #if it's dead --> bring to life?
  #Each dead cell adjacent to exactly 3 living neighbours is a birth cell. It will come alive in next generation.
  if not(isAlive) and count==3:
    nextGen = 'X'
    
  return nextGen

def genNextBoard(board):
  # get rows and cols from the given board
  rows = len(board)
  cols = len(board[0])
  #assemble the board using the parts already created 
  newBoard = createNewBoard(rows,cols)

  #traverse
  for i in range(rows):
    for j in range(cols):
       newBoard[i][j] = getNextGenCell(board, i, j)

    #return the next gen array
  return newBoard

board = createNewBoard(10,10) #initializer
    
    
# print board
print("\nWelcome to the Game of Life")
printBoard(board)

setCell(board, 0, 0, 'X')
setCell(board, 0, 1, 'X')
setCell(board, 1, 1, 'X')
setCell(board, 1, 9, 'X')
setCell(board, 1, 7, 'X')
setCell(board, 2, 8, 'X')
setCell(board, 3, 4, 'X')
setCell(board, 5, 3, 'X')
setCell(board, 3, 2, 'X')
setCell(board, 7, 7, 'X')
setCell(board, 8, 8, 'X')

print("Gen X:")
printBoard(board)
print("--------------------------\n\n")

#repeat the gen multiple times
for i in range(10):
	board = genNextBoard(board)
	print(f"Gen X {i+1}")
	printBoard(board)
	print("--------------------------\n\n")

  
