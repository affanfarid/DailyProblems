'''

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

 

Constraints:

    1 <= nums.length <= 3 * 10^4
    0 <= nums[i][j] <= 10^5



'''

'''
strat:
-recursive
-have a loop to call each recursive function amount of steps
- if value is 2, then loop through 1-2 to check if it works

-recursive end condition is if it reaches the last element
-Some sort of index???
-greatest to least

'''


def jumpGame(arr):
  return jumpGameRec(arr,0)

def jumpGameRec(arr,index):

  #print("---")
  #print("Index is:" + str(index ))
  #print("value is: " + str(arr[index]))

  #reached the end
  if index==len(arr)-1:
    #print("reached end")
    return True
  #overshot
  elif index> len(arr)-1:
    #print("overshot")
    return False
  #recursive call of the values
  else:
    #check
    
    finalBool = False
    #print("checking from 1 to " + str(arr[index]) + " descending order")

    #change from high to low
    for x in range(arr[index],0,-1):
      #print("in loop: " + str(x))
      #rest = jumpGameRec(arr,index+x)
      #print("rest: " + str(rest))
      #finalBool = finalBool or rest

      finalBool = finalBool or jumpGameRec(arr,index+x)
    return finalBool


test1 = [2,3,1,1,4] #true
test2 = [3,2,1,0,4] #false
test3 = [1,1] #true
test4 = [5] #true
test5 = [2,1,1] #true
test6 = [2,0,0,0] #false

print(jumpGame(test1))
    
