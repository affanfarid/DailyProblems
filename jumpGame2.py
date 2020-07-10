'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.

Note:

You can assume that you can always reach the last index.
'''

def jumpGame2(arr):
  minVal = len(arr)+1
  currMinVal = 0
  return jumpGame2Rec(arr, 0, minVal, currMinVal)


def jumpGame2Rec(arr, index, minVal, currMinVal):
  if index==len(arr)-1:
    #print("reached end")
    minVal = min(minVal, currMinVal)
    return minVal
  elif index> len(arr)-1:
    #print("overshot")
    return minVal
  else:
    for x in range(arr[index],0,-1):
      minVal = min(minVal, jumpGame2Rec(arr, index+x, minVal, currMinVal+1) )
    return minVal



test1 = [2,3,1,1,4]
test2 = [1,1,1,1]
test3 = [4,2,3]
print(jumpGame2(test3))
