'''
Last Stone Weight 2
We have a collection of rocks, each rock has a positive integer weight.

Each turn, we choose any two rocks and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

    If x == y, both stones are totally destroyed;
    If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.

At the end, there is at most 1 stone left.  Return the smallest possible weight of this stone (the weight is 0 if there are no stones left.)

 

Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We can combine 2 and 4 to get 2 so the array converts to [2,7,1,8,1] then,
we can combine 7 and 8 to get 1 so the array converts to [2,1,1,1] then,
we can combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we can combine 1 and 1 to get 0 so the array converts to [1] then that's the optimal value.
'''

'''
[6,7,8]
67 - 1,8 -> 7
68 - 2,8 -> 6
86 -> 2,7 -> 5

[2,7,4,1,8,1]
8,1 -> [2,7,4,1,7]
7,1 -> [2,7,4,6]
7,2 -> [5,4,6]
6,4 -> [5,2]
3

biggest 2 smash
[6,7,8]
8,7 -> [1,6] -> 5

[2,7,4,1,8,1]
8,7 -> [2,4,1,1,1]
4,2 -> [2,1,1,1]
2,1 -> [1,1,1]
results in 1


'''

def smashRocks(arr):
  #arrEnum = enumerate(arr)

  while(len(arr)>1):
    #pop the 2 biggest values from the array
    max1 = arr.pop (arr.index(max(arr)) )
    max2 = arr.pop (arr.index(max(arr)) )

    #if they are not equal, add the difference back to the array
    if max1 != max2:
      arr.append(abs(max1-max2))
    #if they equal, they are discarded anyways

  if len(arr) == 0:
    return 0
  else:
    return arr[0]
    


# test1 = [2,7,4,1,8,1]
# test2 = [6,7,8]
# test3 = [2,7,4,1,8]
# print(smashRocks(test3))
