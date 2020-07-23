'''
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3

Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99




'''
#O(n) time
#n space
def singleNum(arr):
  numDict = {}
  for x in arr:
    if x in numDict:
      numDict[x] += 1
    else:
      numDict[x] = 1

  for y in numDict:
    if numDict[y] == 1:
      return y

  return -1


test1 = [2,2,3,2] 
test2 = [0,1,0,1,0,1,99]

print(singleNum(test1)) #3
print(singleNum(test2)) #99

