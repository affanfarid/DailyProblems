'''
Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 

Return the number of negative numbers in grid.

 

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.

Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0

Example 3:

Input: grid = [[1,-1],[-1,-1]]
Output: 3

Example 4:

Input: grid = [[-1]]
Output: 1


'''


def numNegative(arr):
  total = 0
  for m in range(len(arr)):
    for n in range(len(arr[m])):
      if arr[m][n] < 0:
        total += len(arr[m])-n 
        break
  
  return total

test1 = [[3,2],[1,0]]
test2 = [[1,-1],[-1,-1]]
test3 = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]

print(numNegative(test3))

