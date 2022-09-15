# FILENAME cgol.py
# First Last Seth Adams
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: previous work from summer

import random

def createNewBoard (rows, cols):
  board = [[" " for i in range(cols)] for j in range(rows)]
  return board

def printBoard(board):
  rows = len(board)
  cols = len(board[0])

  for x in range(rows):
    for y in rage(cols):
      print(board[x][y], end = "")

def setCell(board, r, c, val):
  board [r][c] = val

def countNeighbours(board, r, c):
  count = 0 #intialize
  for rown in range(r-1, r+2):
    
  
