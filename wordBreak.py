'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

    The same word in the dictionary may be reused multiple times in the segmentation.
    You may assume the dictionary does not contain duplicate words.

Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false


'''

'''
strat:
-loop through letters and find a word.
  -pass in a recursive function of the remaining array
'''

def wordBreaker(word, wordDict):
  if len(word) == 0:
    return True

  for x in range(1,len(word)+1):
    if word[:x] in wordDict:
      return wordBreaker(word[x:], wordDict)

  return False
    

word1 = "leetcode"
wordDict1 = ["leet", "code"]

word2 = "applepenapple"
wordDict2 = ["apple", "pen"]

word3 = "catsandog"
wordDict3 = ["cats", "dog", "sand", "and", "cat"]

print(wordBreaker(word1,wordDict1))
print(wordBreaker(word2,wordDict2))
print(wordBreaker(word3,wordDict3))
