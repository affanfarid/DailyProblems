'''
Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.  For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.

 

Example 1:

Input: ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: one of the longest word chain is "a","ba","bda","bdca".
'''

'''
strat:
find the smallest length strings in the array.

recursive function

abba
abba

cdef
cfdef

ccc
cccc

'''

def validChain2(lesser,greater):
  if len(lesser)+1 != len(greater):
    return False

  #flag allows for only 1 difference
  flag = True
  #compare each string letter by letter
  for x in range(len(lesser)):

    # print(x)
    # print(f"lesser: {len(lesser)}. greater:{len(greater)}")

    #same letter
    if lesser[x] == greater[x]:
      continue
    
    #they are different letters
    else:#if lesser[x] != greater[x]:
      if flag:
        #used up their one "difference"
        flag = False
        #remove the letter
        greater = greater[:x]+greater[x+1:]
        #run the comparison of the same index one more time with the different letter removed
        x -= 1
        continue
      #more than one difference
      else:
        return False
  return True

#DOES NOT WORK FOR ALL CASES, SCRAPPED
def validChain(lesser,greater):
  #creates a temporary string that can be manipulated with
  temp = greater
  #creates a flag because one difference is allowed
  flag = True
  for x in lesser:
    #if the letter is in the greater string, it removes it.
    #the goal is there there should be 1 letter left in temp.
    if x in temp:
      #temp = temp.replace(x,"")
      i = temp.index(x)
      temp = temp[:i] + temp[i+1:]
    else:
      #allows for 1 difference
      if flag:
        flag = False
      else:
        return False
  #if the remaining letters are exactly 1
  if len(temp) == 1:
    temp2 = greater
    #checks if you take it out the letter in the original then it should equal the lesser string. 

    #sus - DOESNT WORK FOR ALL CASES
    if temp2.replace(temp,"") == lesser:
      return True
    else:
      return False

  else:
    return False

def stringChain(arr):
  maxString = [0]
  stringChainRec(arr,"",0,maxString)
  return maxString[0]

def stringChainRec(arr,word,currLen,maxString):
  #print(f"word is: {word}")

  #if the current string is greater than the max, updates the max
  if currLen > maxString[0]:
    maxString[0] = currLen

  #loops through remaining array  
  for x in range(len(arr)):
    #print(f"word: {word} . arr[x]: {arr[x]} ")

    #removes word from the array and makes recursive call increasing the string length
    if validChain(word,arr[x]):
      stringChainRec(arr[:x]+arr[x+1:], arr[x], currLen+1, maxString)



# print(validChain2("ccc","cccc"))
#print(validChain2("abba","aabba"))
#print(validChain2("abba","abcba"))
# test1 = ["a","b","ba","bca","bda","bdca"]
# print(stringChain(test1))
