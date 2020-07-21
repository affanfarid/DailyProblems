'''

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


'''

'''
strat:
-check all sub arrays of index 0:n
-then check all sub arrays of index 1:n, etc
if a product is larger than the current largest, then update it
return the largest value

'''


'''
class Solution {
    public int maxProduct(int[] nums) {
        int max = Integer.MIN_VALUE, imax = 1, imin = 1;
        for(int i=0; i<nums.length; i++){
            if(nums[i] < 0){ int tmp = imax; imax = imin; imin = tmp;}
            imax = Math.max(imax*nums[i], nums[i]);
            imin = Math.min(imin*nums[i], nums[i]);
            
            max = Math.max(max, imax);
        }
        return max;
    }
}


'''

import math

#O(n)
def largestSubArray2(arr):
  maxNum = -500
  imax = -500
  imin = -500
  #count for big O
  count = 0

  #loops through array once
  for x in range(len(arr)):
    #increases count for big O
    count+=1
    #if the number is negative
    if arr[x] < 0:
      #switch imax and imin numbers
      temp = imax
      imax = imin
      imin = temp
    #imax is the max of the current number, or the imax*current numbe
    #same with imin
    imax = max(imax*arr[x] , arr[x])
    imin = min(imin*arr[x], arr[x])

    #maxNumber is the max value of imax and maxNum
    maxNum = max(maxNum, imax)
  
  print("count: "+ str(count))
  return maxNum



#O(n^2)
def largestSubArray(arr):
  count = 0
  largest = 0 

  #double loop for the upper and lower bounds of the subArray
  for x in range(len(arr)):
    for y in range(1,len(arr[x:])+1):
      #used for big O calculation
      count+=1
      #gets the product of the current crafted array within the bounds of [x:y]
      prodTemp = math.prod(arr[x:y])
      #updates the largest product if the product is bigger
      if prodTemp > largest:
        largest = prodTemp

  print("count: "+ str(count))
  return largest


test4 = [-50, 1, 2 ,3]
test1 = [item for item in range(-15,15)]
test2 = [-2,0,-1]
test3 = [2,3,-2,4]

print(largestSubArray(test1))
# print(largestSubArray(test2))
print("--------")
print(largestSubArray2(test1))
#print(largestSubArray2(test2))
