'''
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


'''


'''
strat:
-have a "ifOverlap" function that returns a boolean
-Assume they are in order
-have a index counter
-loop through
  - if counter == len(arr) -1:
    - break
  - if arr[counter] overlaps with arr[counter+1]
    -merge them
  - else: 
    -increase counter



'''
import copy

def ifOverlap(arr1, arr2):
  if arr1[0] < arr2[0]:
    if arr2[0] in range(arr1[0],arr1[1]+1):
      return True
    else:
      return False
  else:
    if arr1[0] in range(arr2[0],arr2[1]+1):
      return True
    else:
      return False



def mergeIntervals(arr):
  finalArr = copy.copy(arr)
  counter = 0

  while(counter < len(finalArr)-1 ):
    if ifOverlap(finalArr[counter],finalArr[counter+1]):
      finalArr[counter][1] = finalArr[counter+1][1]
      del finalArr[counter+1]
    else:
      counter+=1

  return finalArr


# test1 = [1,3]
# test2 = [3,6]
# print(ifOverlap(test1,test2))

test3 = [[1,4],[4,5]]
test4 = [[1,3],[2,6],[8,10],[15,18]]
print(mergeIntervals(test4))
