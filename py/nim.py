# FILENAME nim.py
# First Last Seth Adams
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: previous work from summerimport random
import random
stones = 12
stonesTaken = 0

print("There are " + str(stones) +" stones")

while(stones > 0):
  print(str(stones) + " Remaining")
  playerMove = int(input("How many stones do you want to take? (1-3): "))
  stonesTaken = playerMove 
  while(playerMove > 3 or playerMove < 1 ):
    playerMove = int(input("You can only pick 1-3 stones please revise your guess: "))
    stonesTaken = playerMove
  if(stonesTaken > stones):
    stonesTaken = stones
    print("You cannot have negative stones.  Your guess has been changed to " + str(stones) + " stones")
  stones -= stonesTaken
  if(stones <= 0):
    print("Player Wins")
  else:
    print(str(stones) + " Remaining")
    compChoice = random.randint(1,3)
    print("Computer takes " + str(compChoice) + " stones")
    stones -= stonesTaken
    if(stones <= 0):
      print("Computer Wins")
    
