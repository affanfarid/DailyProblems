'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21


'''

def reverseInt(num):
    neg = False
    numStr = ""
    if num < 0:
        neg = True
    numStr = str(abs(num))
    numStr = numStr[::-1]
    if neg:
        return -1 * int(numStr)
    else:
        return int(numStr)


print(reverseInt(-504))
print(reverseInt(90000))
print(reverseInt(-120))


