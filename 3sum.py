'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]




'''



'''
strat:
-recursive
  -end case is tempArr is full, then check to see if tempArr is to be added to final array or not based on if sum == 0
-overarching for loop
-temp array 


[-1, 0, 1, 2, -1, -4]

if len(tempArr) == 3:
  add to finalArr

  return 

take first element. put it in tempArray
tempArr = [-1]

recursive call passing arr[1:]
[0, 1, 2, -1, -4]
add first element to tempArr
tempArr = [-1,0]

recursive call passing arr[1:]
[1, 2, -1, -4]





'''



def threeSum(arr):
  finalArr = []
  tempArr = []
  threeSumRec2(arr, tempArr, finalArr, 0)
  return finalArr

# def threeSumRec(arr, tempArr, finalArr):


#   if len(tempArr) >= 3:
#     print("got a three set: " + str(tempArr) )
#     if sum(tempArr) == 0:
#       finalArr.append(tempArr[:])
#     #tempArr = tempArr[:-1]
#     #del tempArr[-1]
#     return

#   for x in arr:
#     tempArr.append(x)
#     print("tempArr: "+ str(tempArr))
#     threeSumRec(arr[1:],tempArr,finalArr)
#     tempArr.pop()
#     #del tempArr[-1]



def threeSumRec2(arr,tempArr, finalArr, counter):

  if len(tempArr) == 3:
    print(tempArr)
    
    return

  for x in arr:
    tempArr.append(x)
    threeSumRec2(arr[counter+1:], tempArr, finalArr, counter+1)
    tempArr.pop()


test1 = [-1, 0, 1, 2, -1, -4]
print(threeSum(test1))
