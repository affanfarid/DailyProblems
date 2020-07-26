'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]


'''

'''
strat:
-have an "isPalindrome" function to make things easier

-recursive maybe?
in the case of aaba

the end cases should be

a aba
aa b a
a a b a



a aba - palindrome, but keep going
a a ba -not a palindrome but keep going
a a b a - palindrome but stop because the word is empty

aa ba - aa added to tempArr, keep going with ba
aa b a - added to tempArr but stop because word is empty

aab a - not a palindrome

aaba - not a palindrome



aaba - not a palindrome
aab a - adds a to tempArr, aab isnt a palindrome
aa b a - adds b to tempArr, aa is a palindrome, word is done, now add it to final list
a a b a - adds a to tempArr


a numbered loop in there somewhere

start by checking isPalindrome the whole word
  if it is, add it to the master list
  if its not, take out the first letter, pass in the rest to a recursive function

'''

#checks if its a palindrome
def isPalindrome(word):
  for x in range(len(word)//2):
    if word[x] != word[len(word)-1 -x]:
      return False
  return True

def palPart(word):
  tempArr = []
  finalList = []
  palPartRec(word, tempArr, finalList)
  return finalList

def palPartRec(word, tempArr, finalList):
  #empty word case
  if len(word) == 0 and len(tempArr) == 0:
    return
  #if the word is empty (aka all the palindromes have been added to temp arr)
  #then add it to the final list and return
  elif len(word) == 0:
    finalList.append(tempArr)
    return
  #recursive call
  else:
    #take a partition of the word of every possible length with the first letter
    for x in range(1, len(word)+1):
      #if its a palindrome, add it to the temp arr, and pass in the rest of the word recursively
      if isPalindrome(word[:x]):
        palPartRec(word[x:], tempArr + [word[:x]], finalList)




# test1 = "aaba"
# print(palPart(test1))