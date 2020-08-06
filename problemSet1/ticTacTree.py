'''
In the game Tic Tac Tree, an N x N board is filled with red and black game pieces, with one piece per cell. The “red” and “black” players receive 1 point for every
sequence of three consecutive cells of the same color pieces, whether that sequence is horizontal, vertical, or diagonal. Each three-cell sequence counts as one
point. For example, a horizontal row of 4 red pieces is worth 2 points, and a vertical column of 6 black pieces is worth 4 points. Write a function that, given a
Boolean array with the distribution of red and black pieces, will return the winner of the game.


'''


'''
strat:

loop through 2d array

at each position, check for 3 in a row, to the right, down and diagon downright

if there are 3 in a row, increase score by 1

have seperate scores for player 1 and player 2

return the winner as a boolean (pl true, p2 false)

recursive strat:

for the check function:

pass along a boolean

pass along a counter which decreases each pass, initial counter is how many in a row you want to check
if counter reaches 0 or the current boolean is different, you return false

otherwise you pass along next index

problem: would need some sort of “direction indicator" so you dont go down and then diagonal
IDEA SCRAPPED

'''

def check3(x,y,arr):
  total = 0
  #out of bounds, so returns false
  if x+2 > len(arr)-1:
    return 0
  if y+2 > len(arr[0])-1:
    return 0
  
  #going right
  if arr[x][y] == arr[x+1][y] and arr[x][y]==arr[x+2][y]:
    total += 1
  #going down
  if arr[x][y] == arr[x][y+1] and arr[x][y]==arr[x][y+2]:
    total += 1
  #diagonal
  if arr[x][y] == arr[x+1][y+1] and arr[x][y]==arr[x+2][y+2]:
    total += 1
  
  return total


def ticTacTree(arr):
  trueScore = 0
  falseScore = 0
  
  for x in len(arr):
    for y in len(arr[0]):
      #square is true
      if arr[x][y]:
        trueScore += check3(x,y,arr)
      #square is false
      else:
        falseScore += check3(x,y,arr)
  
  return trueScore >= falseScore
