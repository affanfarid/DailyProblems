'''
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

Note:
You may assume that you have an infinite number of each kind of coin.


'''

'''
strat is to subtract as many of max, when you cant any more, then subtract the next lowest

ex. coins = [2,5] amount = 26

subtract max, which is 5. 21
  subtract max, which is 5. 16
    subtract max, which is 5. 11
      subtract max, which is 5. 6
        subtract max, which is 5. 1
          subtract max, doesnt work cause its -4
        subtract next biggest, which is 2, doesnt work cause its -1
      subtract next biggest which is 2, 4. 
        subtract 




'''


def coinChange(arr, goal):
  #sorts the array so it always tests biggest coin first
  arr.sort(reverse=True)
  return coinChangeRec(arr, goal, 0)

def coinChangeRec(arr,goal,numCoins):
  #if its negative, then return -1
  if goal < 0:
    return -1
  #this means the goal has been met, so return the number of coins
  elif goal == 0:
    return numCoins
  else:
    #test every coin, biggest first
    for x in range(len(arr)):
      temp = coinChangeRec(arr,goal-arr[x], numCoins+1)
      if temp < 0:
        continue
      #the first value to be met is always the lowest number of coins, so the loop can be broken out of
      else:
        break
      
    return temp


tArr1 = [1, 2, 5]
tG1 = 11

tArr2 = [2]
tG2 = 3

tArr3 = [2,5]
tG3 = 26

print(coinChange(tArr1,tG1)) #3
print(coinChange(tArr2,tG2)) #-1
print(coinChange(tArr3,tG3)) #7