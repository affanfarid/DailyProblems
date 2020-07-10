'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

 

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:

Input: m = 7, n = 3
Output: 28

x x x
x x x

'''
def uniquePaths(m,n):
  total = 0
  return uniquePathsRec(m-1,n-1,total)


def uniquePathsRec(m,n,total):
  if m == 0 and n == 0:
    total += 1
    return total
  elif m == 0:
    return uniquePathsRec(m,n-1,total)
  elif n == 0:
    return uniquePathsRec(m-1,n,total)
  else:
    return uniquePathsRec(m-1,n,total) + uniquePathsRec(m,n-1,total)



test1 = uniquePaths(7,3)
print(test1)
