'''
The letters of a secret password have been embedded, in order, in an alpha-only string at index numbers N, 2N, 3N ... N42 where the value of N starts at 4 and
increases until the string can no longer support N*2. Index numbers start at 1. The criteria for the password are:

-The first and last characters of the password must be uppercase.

-The password must contain at least three vowels, which can be either uppercase or lowercase.

-If the password has an odd number of characters, the middle character of the password must be a vowel (A/a, E/e, I/i, O/o, or U/u).

-If the password has an even number of characters, the middle two characters of the password must be the same vowel, and must both be either uppercase or lowercase.

Write a function that, given a string, will print all possible passwords embedded in the string that meet these criteria. For example, if the string passed in is

“zzzAEzzazPzazzIWzzzCzzzzE", the output should be:

AaaW EPICE

Note that Aaaw is the password when N=4 and EPICE is the password when N=5.

'''

def isVowel(letter):
  return  letter.lower() in ["a","e","i","o","u"]

def vowelCount (word):
  vowelCount = 0
  for x in word:
    if isVowel(x):
      vowelCount += 1
  return vowelCount


def password(str1):
  passList = []
  #constructs the potential passwords
  #goes through all the possible N's
  for x in range(len(str1)):
    temp = ""
    for y in range(0,len(str1),x):
      temp += y
    passList.append(temp)

  for word in passList:
    if not (word[0].isUpper() and word[-1].isUpper() ):
      continue
    if vowelCount(word) < 3:
      continue
    #checks if odd number of chars, then middle must be a vowel
    if len(word)%2 == 1:
      if not isVowel(word[len(word)/2]):
        continue
    else:
      if not ( word[len(word)/2] == word[len(word)/2 +1] and isVowel(word[len(word)/2]) ):
        continue
  print (word)
