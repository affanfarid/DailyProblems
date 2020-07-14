'''

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).



'''


'''
strat:
-number of letters accounts of the "longest" Code. 
-loop through 
-recursive


'''

alphabetDict = {1:"A", 2:"B", 3:"C", 4:"D", 5:"E", 6:"F", 7:"G", 8:"H", 9:"I", 10:"J", 11:"K", 12:"L", 13:"M", 14:"N", 15:"O", 16:"P", 17:"Q", 18:"R", 19:"S", 20:"T", 21:"U", 22:"V", 23:"W", 24:"X", 25:"Y", 26:"Z" }


def encoded(code):
  count = 0
  return encodedRec(code,count)



def encodedRec(code, count):
  print("count: " + str(count))
  if len(code) == 0:
    print("added 1")
    count+=1
    return count
  else:
    print("code: " + code)

  if len(code) >= 2: #has enough space for 2 digits
    if int(code[0]) == 1:
      count = encodedRec(code[2:],count)

    elif int(code[0]) == 2 and int(code[1]) in range(0,7):
      count = encodedRec(code[2:],count)

  count = encodedRec(code[1:],count)
  
  return count


test1 = "226"
test2 = "12"

print(encoded(test2))
