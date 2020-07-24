'''
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

    Only one letter can be changed at a time.
    Each transformed word must exist in the word list.

Note:

    Return 0 if there is no such transformation sequence.
    All words have the same length.
    All words contain only lowercase alphabetic characters.
    You may assume no duplicates in the word list.
    You may assume beginWord and endWord are non-empty and are not the same.

Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.


'''

'''
strat:
recursive
have a function where it detects if one letter is different- returns boolean

loop through potential words and if they are one letter off, make that word the new word, and remove it from the wordList being passed in

also have some sort of count passed down

'''

def oneLetterOff(word1, word2):
  #assumes the words are of equal length
  numLettersOff = 0
  for x in range(len(word1)):
    if not word1[x] == word2[x]:
      numLettersOff += 1
  
  if numLettersOff <= 1:
    return True
  else:
    return False


def wordLadder(begin, end, wordList):
  #supposed to be the system max, just picked a really high number
  ultMax = 5000
  return wordLadderRec(begin, end, wordList, 0, ultMax, ultMax )

def wordLadderRec(begin, end, wordList, count, minVal, constMax):
  
  #print(wordList)
  #print(end in wordList)

  #if the begin word is equal to the end word, return the count +1 
    # +1 because the beginning word isnt counted
  if begin == end: #oneLetterOff(begin,end):
    #print("found!: " + str(count+1))
    return count + 1
  #if the end word isnt in the wordList, save the hassle and just return 0
    #exception to this would be if begin and end are equal, in that case
    #it gets handled in the if statement above this one
  elif end not in wordList:
    return 0
  else:
    #print("begin: " + begin)
    #for each word in the list, 
    for x in range(len(wordList)):
      #it checks if its one letter off
      if oneLetterOff(begin,wordList[x]):
        #if it is, remove the word from the list that it is "transforming"
          #to, and then increase the count by 1
        temp = wordLadderRec(wordList[x], end, wordList[:x]+wordList[x+1:], count+1, minVal, constMax)
        #if its greater than 0 (omits dead ends)
        if temp > 0:
          #the minimum value is the lesser of the current min value and 
            #the number derived from that path
          minVal = min(minVal, temp)
    
    #if the minVal is equal to the constant max, it means it cycled 
      #through the whole list and nothing was one letter off of begin
      #therefore we return 0
    if minVal == constMax:
      return 0
    #otherwise return the minimum Value
    else:
      return minVal
    

test1 = ["hot","dot","dog","lot","log","cog"]
test2 = ["hot","dot","dog","lot","log"]
test3 = ["hot","dot","dog","lot","log","cog"]
test4 = ["hot","dot","dog","lot","log","cog","dol"]
test5 = test1
test6 = []

print(wordLadder("hit","cog",test1)) #5
print(wordLadder("hit","cog",test2)) #0

#pog - cog
print(wordLadder("pog","cog",test3)) #2

#cot - dot - dol
print(wordLadder("cot","dol",test4)) #3

#no correlation
print(wordLadder("pis","cog",test5)) #0

#list is empty
print(wordLadder("hit","cog",test6)) #0
