'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''

def longestSubstring(s):
  usedLetters = []
  maxSubstring = 0
  currSubstring = 0

  
  for x in s:

    currSubstring+=1

    if x in usedLetters:
      currSubstring = 1
      usedLetters = [x]
    else:
      usedLetters.append(x)

    if currSubstring > maxSubstring:
      maxSubstring = currSubstring
      #print("changed")
    
    #print(usedLetters)
    #print(currSubstring)

  return maxSubstring

test1 = "abcabcbb"
test2 = "bbbbb"
test3 = "pwwkew"


print(longestSubstring(test1))
print(longestSubstring(test2))
print(longestSubstring(test3))
