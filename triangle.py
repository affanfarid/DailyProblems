'''
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.


'''

'''
strat:
-each node can access exactly 2 nodes beneath it:
  find the equation given l as the length of the row of the triangle,
  and n as the position in the row

  l is len(arr[x])
  and n starts at index 0

  for example, l is 3 and n is 1. that means it can access indecies 1 and 2 in the row where l = 4

  another example, l = 2, n = 1, that means it can access 1 or 2 in l=3

  so the numbers it can access are n and n+1 in the next row

-recursive
-pass down the sum 

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

'''


def triangle(arr):
  return triangleRec(arr,0,0,0)


def triangleRec(arr, row, index, sumVal,):
  #reached the bottom row
  if row == len(arr) - 1:
    return sumVal + arr[row][index]
  else:
    #returns the minimum sum of the two branches
    return min(
      triangleRec(arr, row+1, index, sumVal+arr[row][index] ) ,
      triangleRec(arr, row+1, index+1, sumVal+arr[row][index] )
    )


test1 = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

test2 = [
     [0],
    [1,1],
   [2,2,2],
  [1,2,2,3]
]

print(triangle(test1)) #11
print(triangle(test2)) #4


