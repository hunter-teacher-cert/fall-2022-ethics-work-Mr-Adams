import random
import math

def createdList(length) :
  randomList = []
  for i in range(length):
    n = random.randint(0,10)
    randomList.append(n)
  return randomList

def binSearch(list, value):
  low = 0
  high = len(list)-1
  mid = 0

  while(low <= high):
    mid = (high + low)//2
    if list[mid] == value:
      return(mid)
    elif (value < list[mid]):
      high = mid - 1
    else:
      low = mid + 1

testList = createdList(20)
print(testList)
testList.sort()
print(testList)
print("5 is at index: ")
print(binSearch(testList, 5))
