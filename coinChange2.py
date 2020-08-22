'''

You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

 

Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:

Input: amount = 10, coins = [10] 
Output: 1



'''


'''
strat:
for every coin, if its less than the current amount, subtract that, and pass that in recursively


'''

def coinChange2(amount, coins):
    #finalArr = [0]
    comboArr = []

    coinChange2Rec(amount, coins, [], comboArr)
    
    return len(comboArr)

def coinChange2Rec(amount, coins, tempArr, comboArr):
    if amount == 0:
        if sorted(tempArr) not in comboArr:
            comboArr.append(sorted(tempArr))
        return
    elif amount < 0:
        return
    else:
        for x in coins:
            if x <= amount:
                coinChange2Rec(amount-x, coins, tempArr + [x], comboArr)



print(coinChange2(5, [1,2,5]))
print(coinChange2(3, [2]))
print(coinChange2(10, [10]))
