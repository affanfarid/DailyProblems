'''

You are given a string s that consists of lower case English letters and brackets. 

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.

 

Example 1:

Input: s = "(abcd)"
Output: "dcba"

Example 2:

Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.

Example 3:

Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.

Example 4:

Input: s = "a(bcdefghijkl(mno)p)q"
Output: "apmnolkjihgfedcbq"


'''

'''
strat:
have a begin. where it senses the beginning (
    then it loops through the rest to find its end.
    if it finds another ( then recursively call itself. 

when it finds ). it flips from the beginning of the string.

'''



def func1(input):
    return flipperHelper(input)


def flipperHelper(input):
    print(input)
    for x in range(len(input)):
        print(x)
        if input[x] == "(":
            temp = flipperHelper(input[x+1:])
            input = input[:x] + temp
            #???? v
            x += 1
        if input[x] == ")":
            rev = input[:x]
            print(rev) 
            return rev[::-1] + input[x+1:]


test1 = "a(bcdefghijkl(mno)p)q"
print(func1(test1))
        



