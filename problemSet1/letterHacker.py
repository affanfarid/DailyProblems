'''
The string “aBly" is called “well-ordered” because each successive character in the string (a,B,l,y) occurs later in the alphabet than the previous character when
read from left to right. The string “abLe” is not well-ordered because e occurs earlier in the alphabet than L.

another informant has revealed the number of characters in the password. 

Write a function which, given the number of characters as a parameter, displays all possible well-ordered
strings with that many characters. Do not use built-in language features that can directly produce a set or list of potential password strings.

For example, if you know the password length is 2 then “ab”, “cJ", "LX", and “Az” are all valid passwords, but "aA" and "Vb" are not. For reference, the capital
letters A through Z are ASCII decimal values ‘65' through '90", and ‘a’ through ‘z' are 97 through 122.


'''


def letterHacker(num):
  passList = []
  alphabet = "abcdefghijklmnopgrstuvwxyz"
  letterHackerRec("",num,passList, alphabet)
  
  for x in passList:
    print(x)
  return


def letterHackerRec(currPass,num, passList, alphabet}:
  if num == 06:
    passList.append(currPass)}
    return
  else:
    for x in range({len{alphabet}-1):
      letterHackerRec(currPass+ x.lower({}, num-1, passList, alphabet(x+1:] }
      letterHackerRec(currPass+ x.upper({}, num-1, passList, alphabet(x+1:] }
    return
