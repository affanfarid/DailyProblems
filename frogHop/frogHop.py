'''
A frog is crossing a river. The river is divided into x units and at each unit there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog is able to cross the river by landing on the last stone. Initially, the frog is on the first stone and assume the first jump must be 1 unit.

If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units. Note that the frog can only jump in the forward direction.

Note:

    The number of stones is ≥ 2 and is < 1,100.
    Each stone's position will be a non-negative integer < 231.
    The first stone's position is always 0.

Example 1:

[0,1,3,5,6,8,12,17]

There are a total of 8 stones.
The first stone at the 0th unit, second stone at the 1st unit,
third stone at the 3rd unit, and so on...
The last stone at the 17th unit.

Return true. The frog can jump to the last stone by jumping 
1 unit to the 2nd stone, then 2 units to the 3rd stone, then 
2 units to the 4th stone, then 3 units to the 6th stone, 
4 units to the 7th stone, and 5 units to the 8th stone.

Example 2:

[0,1,2,3,4,8,9,11]

Return false. There is no way to jump to the last stone as 
the gap between the 5th and 6th stone is too large.

'''

'''
strat:
recursive function, try with k+1, then k, then k-1, all paths

have a jumpAmount 



'''

#O(n) solution
def frogHop(arr):
  return frogHopRec(arr,0,arr[0])

def frogHopRec(arr, jump, prev):
  #print("prev: {}".format(prev) )

  #reached the end of the array/last stone
  if len(arr) <= 1:
    return True
  else:
    boolVal = False

    #loops through the rest of the stones to check valid path
    for x in range(len(arr)):
      #sees if it can jump to k-1, k, or k+1 distance to stone
      for k in range(jump-1,jump+2):
        #if k is negative or 0, then infinite loop so this fixes that
        if k<=0:
          continue
        #if the stone is "valid", then it recursively jumps to next stone
        if k+prev == arr[x]:
          #if one solution has already been found then no extra calls are needed cause boolVal is already true
          boolVal = boolVal or frogHopRec(arr[x:], k, arr[x])

    return boolVal


# test1 = [0,1,2,3,4,8,9,11]
# test2 = [0,1,3,5,6,8,12,17]


# test3 = [0,1,3,6,10,15,21]
# test4 = [num for num in range(0,100)]

# print(jumpGame(test4))

