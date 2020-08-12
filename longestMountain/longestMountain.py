'''
Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

    B.length >= 3
    There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]

(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain. 

Return 0 if there is no mountain.

Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.

Example 2:

Input: [2,2,2]
Output: 0
Explanation: There is no mountain.

Note:

    0 <= A.length <= 10000
    0 <= A[i] <= 10000

Follow up:

    Can you solve it using only one pass?
    Can you solve it in O(1) space?


'''

'''
strat:
have 2 pointers go through the list.
a mountain starts when p1<p2.
mountain ends when p1>p2

have a current Greatest variable

if the mountain ends, update the current greatest variable.

have a mountainstart variable. 

[2,1,4,7,3,2,5]
longest is:
  [1,4,7,3,2]

1 4. rising. 
4 7. rising.
7 3. falling.
3 2. falling.
2 5. rising. mountain ends at 2. 
-
only need to check falling with boolean variable

'''

def longestMountain(arr):
  #if arr is empty return 0
  if len(arr) == 0:
    return 0

  longest = 0
  currLongest = 0
  falling = False

  #loop through array except last one
  for x in range(len(arr)-1):
    #rising
    if arr[x] < arr[x+1]:
      currLongest += 1
      #if it was falling and now is rising again, the mountain ended
      if falling:
        #update the longest and reset the other values
        longest = max(longest,currLongest)
        currLongest = 1
        falling = False

    #falling
    if arr[x] > arr[x+1]:
      falling = True
      currLongest += 1

  #in case the array ends with the mountain
  return max(longest,currLongest+1)


