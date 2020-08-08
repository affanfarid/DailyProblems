'''
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.



'''

''''
tree
t:1
r:1
e:2

[]
loop through dict.
t
[t]
r
[t,r]



'''

def sortFreq(word):

  letDict = {}
  letArr = []
  finalString = ""

  #maxFreq = 0 
  for x in word:
    if x in letDict:
      letDict[x] += 1
    else:
      letDict[x] = 1

  print(letDict)

  for y in letDict:
    if len(letArr) == 0:
      letArr.append(y)
    else:
      for z in range(len(letArr)):
        if letDict[y] <= letDict[letArr[z]]:
          letArr.insert(z,y)
          break
        else:
          letArr.insert(0,y)
          break
 
  print(letArr)

  for letter in letArr:
    for x in range(letDict[letter]):
      finalString+= letter

  return finalString


test1 = "tree"
test2  = "cccaaa"
test3 = "Aabb"

print(sortFreq(test3))

