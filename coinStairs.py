'''
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.

Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤ 

Because the 4th row is incomplete, we return 3.

'''

def coinStairs(n):
  temp = n
  counter = 1
  while(temp >= counter):
    # print("temp "+ str(temp))
    # print("counter "+ str(counter))
    
    temp -= counter
    counter += 1
    
  return counter - 1


print(coinStairs(1)) #1
print(coinStairs(3)) #2
print(coinStairs(4)) #2
print(coinStairs(6)) #3
print(coinStairs(10)) #4
