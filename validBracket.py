'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.


'''


'''
have a dictionary of the open bracket as key and closed bracket as value

loop through the string
if the char is in the inputDict then push the value (closed bracket) onto stack

if its the same char as the top of the stack, then pop it
otherwise return false

return true if stack is empty

'''

def isValid(s: str) -> bool:


  inputDict = {
    "(": ")",
    "{": "}",
    "[": "]"
  }
    
  if len(s)%2 == 1:
      return False
  
  stack = []

  for x in s:
      if x in inputDict:
        stack.append(inputDict[x])
      elif stack[len(stack)-1] == x:
        stack.pop()
      else:
        return False
  
  if len(stack)==0:
    return True
  else:
    return False
        


exInput1 = "[]"
exInput2 = "[{}()]"
exInput3 = "[{}{()]"
exInput4 = "[{}{)()]"

print( isValid(exInput3) )









