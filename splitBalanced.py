'''
Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.

 

Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

Example 2:

Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.

Example 3:

Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".

Example 4:

Input: s = "RLRRRLLRLL"
Output: 2
Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'



'''

'''
strat:

'''


def splitBalanced(word):
    totalArr = [0]
    splitBalancedRec(word,totalArr)
    return totalArr[0]

def splitBalancedRec(word,arr):
    numL = 0
    numR = 0
    if len(word) == 0:
        return 

    for x in range(len(word)):
        if word[x] == 'L':
            numL += 1
        elif word[x] == 'R':
            numR += 1
        if numL == numR and numL != 0:
            arr[0] += 1
            splitBalancedRec(word[x+1:],arr)
            break


print(splitBalanced("RLRRLLRLRL")) #4
print(splitBalanced("RLLLLRRRLR")) #3
print(splitBalanced("LLLLRRRR")) #1
print(splitBalanced("RLRRRLLRLL")) #2
