'''
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3

Example 2:

Input: [3,4,-1,1]

Output: 2

Example 3:

Input: [7,8,9,11,12]
Output: 1

Note:

Your algorithm should run in O(n) time and uses constant extra space.
'''


'''

strat:
run through the list once

dictionary
(may change)

[2,3,4,5,1]
loop thorugh and add to dict 

O(n)

loop through again
while spi not in dict 
spi += 1

O(n)

return n


---

ex. [2,5,1,-10,50]

the spi MUST fall into the range of [1,...,len(arr)+1]
this is because if you have [1,2,3] it has to be 4 in this case,
and if any of the numbers were negative or greater than 3, then the 
"hole" would be between 1 and len(arr), or in this case, between 1 and 3.

Therefore to cover both cases, spi must fall in range [1,...,len(arr)+1]


we CAN manipulate the original array

loop through the whole array
first we throw out any element that is not within the 
range of [1,...,len(arr)+1]

by "throwing them out", change the value of those to 0

in this case, len(arr+1) == 6

so our array becomes [2,5,1,0,0]

SPACE needs to be constant, so we cant have a dictionary

loop through new array
for x in arr:
  temp = arr[x]
  arr[x] = temp








---

{2,3,4,5,1}
spi => 2,3,4,5,6

n*n-1


'''

def test(numList):
  spi = 1
  numDict = {}
  for x in numList:
    numDict[x] = True
    
    if x == spi:
      while(spi not in numDict):
        spi+=1




def findMissingPositive(numList):
  spi = 1
  minVal = 0
  maxVal = 0

  numDict = {}

  for x in numList:

    numDict[x] = True
 
    if x > maxVal:
      maxVal = x
    if x < minVal:
      minVal = x



    if x == spi:
      spi+=1
    
  
  return spi


test1 = [1,2,0]
test2 = [3,4,-1,1]
test3 = [7,8,9,11,12]
test4 = [2,3,4,5,1]

print(findMissingPositive(test1))
print(findMissingPositive(test2))
print(findMissingPositive(test3))
print(findMissingPositive(test4))
