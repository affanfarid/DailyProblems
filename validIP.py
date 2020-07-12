'''

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

A valid IP address consists of exactly four integers (each integer is between 0 and 255) separated by single points.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]

'''

'''
strat:
-recursive???
-counter cause you need exactly 4 numbers
pass in array, a for loop for the first 4 elements, then 3 elements etc.
  -gotta check at every loop if its between 0-255
  -if its not then simply return


'''


def validIP(ipStr):
  finalArr = []
  counter = 4
  tempStr = ""
  validIPRec(ipStr,finalArr,counter, tempStr)
  return finalArr

def validIPRec(ipStr,finalArr,counter, tempStr):
  if counter == 0 and len(ipStr) == 0:
    finalArr.append(tempStr[:len(tempStr)-1])
    return 
    #change???

  elif counter == 0 and len(ipStr) > 0:
    #dead end
    return
  else:
    #goes 1,2,3,4
    for x in range(1,4):
      if int(ipStr[0:x]) >= 0 and int(ipStr[0:x]) <= 255:
        validIPRec(ipStr[x:], finalArr, counter-1, tempStr+ipStr[0:x]+"."  )
      else:
        continue
      #tempStr += ipStr[0:x] + "."
      #part of the IP we are sepearating
      #ipStr[0:x]
      #rest of the IP address string
      #ipStr[x:]
      

test1 = "25525511135"
print(validIP(test1))


