'''
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

'''

'''
strat:
a peak is where the PREVIOUS and AFTER number are both smaller


---
example:
[6,7,8,9,1]

'''

#O(n)
def peakElement(arr):
  peakIndex = -1
  maxValue = 0
  for x in range(len(arr)):
    if x == 0:
      maxValue = arr[x]
      peakIndex = x
    #on last element
    elif x == len(arr)-1:
      if arr[0] > arr[x]:
        return 0
      else:
        return x
    elif arr[x] > arr[x-1] and arr[x] > arr[x+1]:
      return x
  return peakIndex

#O(log(n))
def peakElement2(arr):
  return peakElement2Rec(arr,(len(arr)-1)//2)


'''
example:
[6,7,8,9,1]
--
[2,3,4,5,6,7,8,9,1]
[6,7,8,9,1]
[8,9,1]
returns 9

--
[2,9,4,19,20,27,11,20,50]
20 is mid, its on an ascending slope -> take right half
[20,27,11,20,50]]
11 is mid, its on a descending slope -> take left half
[20,27,11]
27 is a Peak! Done


--
strat:
start at middle index of array:
if its an edge:
  ???
if its a peak (both left and right are less):
  return the peak index

'''
def peakElement2Rec(arr,midIndex):
  print("arr: "+str(arr))
  print("midIndex: " + str(midIndex))
  mid = ( len(arr)-1 )//2

  
  if len(arr) == 0:
    return -1
  elif len(arr) == 1:
    return midIndex
  elif len(arr) == 2:
    #reached right end
    if midIndex == len(arr)-1:
      if arr[0] > arr[1]:
        return midIndex-1
      else:
        return midIndex
    #reached left end
    elif midIndex == 0:
      if arr[0] > arr[1]:
        return midIndex
      else:
        return midIndex+1
      
  
  
  #this is a peak
  if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
    return midIndex
  #on ascending slope -> go right
  elif arr[mid] > arr[mid-1] and arr[mid] < arr[mid+1]:
    #only searches half the array, and increases mid index by half the length of the new array
    return peakElement2Rec(arr[mid:], midIndex+((len(arr[mid:])-1)//2) ) 
  #descending slope -> Go left
  elif arr[mid] < arr[mid-1] and arr[mid] > arr[mid+1]:
    #only searches half the array, and decreases mid index by half the length of the new array
    return peakElement2Rec(arr[:mid+1], midIndex-((len(arr[:mid+1])-1)//2) ) 
    

    

test1 = [1,2,3,1] #should return 2
test2 = [1,2,1,3,5,6,4] # should return 1 or 5
test3 = [1,9] #return 1
test4 = [9,1] #return 0
test5 = [6,7,8,9,1] #return 3

print(peakElement2(test5))
