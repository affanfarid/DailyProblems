#a child is running up a staircase with n steps and can hop either 1, 2 or 3 steps at a time. implement a method to count how many possible ways the child can run up the stairs 

'''

Example: 1

1

Ex: 2
1, 1
2

ex. 3
1, 1, 1
1, 2
2, 1
3


--
1, 1, 1, 1, 1
1, 2, 1, 1



'''


#total = 0

def numPossibleWays(n):
  if (n<0):
    return 0
  if (n==0):
    return 1
  else:
    return numPossibleWays(n-1) + numPossibleWays(n-2) + numPossibleWays(n-3)


print(numPossibleWays(3))
