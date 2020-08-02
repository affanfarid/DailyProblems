'''
Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

Return the power of the string.

 

Example 1:

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.

Example 2:

Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

Example 3:

Input: s = "triplepillooooow"
Output: 5

Example 4:

Input: s = "hooraaaaaaaaaaay"
Output: 11

Example 5:

Input: s = "tourist"
Output: 1



'''
#O(n) time
def consecChars(word):
  maxLen = 0
  
  for x in range(len(word)-1):
    n = x+1
    temp = 1
    while(word[n]==word[x]):
      temp += 1
      n+=1
      if n+1 >= len(word):
        break
    x = n
    maxLen = max(maxLen,temp)

  return maxLen

print(consecChars("leetcode")) #2
print(consecChars("abbcccddddeeeeedcba")) #5
print(consecChars("triplepillooooow"))  #5
print(consecChars("hooraaaaaaaaaaay")) #11
print(consecChars("tourist"))   #1
    
