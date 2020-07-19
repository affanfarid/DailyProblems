'''
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"

Example 2:

Input: [3,30,34,5,9]
Output: "9534330"

Note: The result may be very large, so you need to return a string instead of an integer.


'''

'''
[98,8]
988

330

strat:
-sort by first digit in descending order
-then sort by 2nd digit in descending order
-etc

3
compare each digit


strat2:
-insert first number into finalArray
-loop through rest of array
COMPARISON:
-if first digit of x in array is greater than y in finalArray
  -insert it there
- if first digit of x in array is less than y in finalArray
  -move past it and do comparison again
-if digits are equal
  -do a comparison on the rest of the digits


3 30
303
330

3 is prioritized over 30

3 39
339
393

now 39 is prioritized over 3

3 34
334
343 <---

3 32
332 <---
323

Input: [3,30,34,5,9]


3
compare 30 with 3. 
330 > 303
now its 3,30
trying to add 34
334 with 343
343 > 334
add 34 before 3
34,3,30
trying to add 5
534 > 345
add 5 before 34
5,34,3,30
trying to add 9
95 > 59
9 is added before 5
9,5,34,3,30

"9534330"

'''

'''
TIME COMPLEXITY:
at least n for going through each element in the initial list
ex. 5+4+3+2+1
triangle number
which is:

(n^2 + n)/2

which is pretty much n^2

'''

def isNum1GTNum2(num1, num2):
  n1 = str(num1)
  n2 = str(num2)

  if int(n1+n2) >= int(n2+n1):
    return True
  else:
    return False



def largestNum(arr):
  arrFinal = []
  count = 0
  for x in arr:
    
    #may need to change looping by index
    flag = True
    for y in range(len(arrFinal)):
      count += 1
      if isNum1GTNum2(x, arrFinal[y]):
        #insert x before y in the final array
        arrFinal.insert(y,x)
        flag = False
        break
    if flag:
      arrFinal.append(x)

  print(count)

  finalStr = ""
  for z in arrFinal:
    finalStr+= str(z)

  return finalStr
      

test1 = [3,30,34,5,9] #"9534330"
test2 = [9, 5, 34, 3, 30] #"9534330"
test3 = [30, 3, 34, 5 ,9] #"9534330"
test4 = [10,2] #210
test5 = [item for item in range(0,15)] #98765432141312111100
print(largestNum(test5))
