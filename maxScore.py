'''
Given an array A of positive integers, A[i] represents the value of the i-th sightseeing spot, and two sightseeing spots i and j have distance j - i between them.

The score of a pair (i < j) of sightseeing spots is (A[i] + A[j] + i - j) : the sum of the values of the sightseeing spots, minus the distance between them.

Return the maximum score of a pair of sightseeing spots.

 

Example 1:

Input: [8,1,5,2,6]
Output: 11
Explanation: i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11

'''

def getScore(arr,i,j):
  return arr[i] + arr[j] + i -j

def sightScore(arr):
  maxScore = 0
  for x in range(len(arr)-2):
    for y in range(x+1,len(arr)-1):
      currScore = getScore(arr,x,y)
      if currScore > maxScore:
        maxScore = currScore

  return maxScore

test1 = [8,1,5,2,6]
print(sightScore(test1))
