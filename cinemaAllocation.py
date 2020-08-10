'''

A cinema has n rows of seats, numbered from 1 to n and there are ten seats in each row, labelled from 1 to 10 as shown in the figure above.

Given the array reservedSeats containing the numbers of seats already reserved, for example, reservedSeats[i] = [3,8] means the seat located in row 3 and labelled with 8 is already reserved.

Return the maximum number of four-person groups you can assign on the cinema seats. A four-person group occupies four adjacent seats in one single row. Seats across an aisle (such as [3,3] and [3,4]) are not considered to be adjacent, but there is an exceptional case on which an aisle split a four-person group, in that case, the aisle split a four-person group in the middle, which means to have two people on each side.

 

Example 1:

Input: n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
Output: 4
Explanation: The figure above shows the optimal allocation for four groups, where seats mark with blue are already reserved and contiguous seats mark with orange are for one group.

Example 2:

Input: n = 2, reservedSeats = [[2,1],[1,8],[2,6]]
Output: 2

Example 3:

Input: n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
Output: 4



'''

'''
strat:
groups can only sit in the same ROW, not column

find how many can sit in that row, and do that for every row 

loop through the Row. 
if the seat is empty, add 1 to a counter.
if its occupied, reset the counter to the counter to 0.
if the counter reaches 

aisle= [4,8]

'''

def groupIsValid(groupBlock, groupSize, aisleSep):
  if len(groupSize) < groupSize:
    return False

  for x in groupBlock:
    

  return


def groupsInRow(resSeats, rowNum, groupSize, aisleSep, rowSize):
  validGroups = [
    [2,3,4,5],
    [4,5,6,7],
    [6,7,8,9]
  ]

  for x in validGroups


  counter = 0
  openSeatBlocks = []
  total = 0
  temp = []
  for x in range(1,rowSize+1):
    if [rowNum, x] in resSeats:
      counter = 0
      if len(temp) != 0:
        openSeatBlocks.append(temp)
      temp = []
    else:
      counter += 1
      temp.append(x)
  if len(temp) != 0:
    openSeatBlocks.append(temp)

  #for each block, check the size == groupSize

  validblocks = [[2,3,4,5],[4,5,6,7],[7,8,9,10]]


  for x in openSeatBlocks:
    if len(x) >= groupSize:


    # if counter == groupSize:
    #   openSeatBlocks.append(temp)
    #   temp = []

  print(openSeatBlocks)

  return total

def cinemaAllocation(resSeats,numRows):
  aisleSep = [3,7,10]
  groupSize = 4
  rowSize = 10
  totalGroups = 0
  for x in range(1,numRows+1):
    totalGroups += groupsInRow(resSeats, x, 4, aisleSep, rowSize)

  return groupSize

r1 = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
n1 = 3
cinemaAllocation(r1,n1)
