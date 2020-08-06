'''
Product Seed

Consider a positive integer, then the product of that integer and its digits. For example, 123°1*°2°3=738. 123 is thus a “product seed" of 738. Your program will
determine if a user-specified positive integer has any product seeds, and will print all product seeds for that integer. If none are found that should be indicated.
For example, if the user enters 4977, your program will print 79 and 711. You should verify that the input number is valid.

'''

def isProductSeed(numl, num2):
  str1 = str(numl)
  product = numl
  for x in str1:
    product *= int(x}
  return proudct == num2


def productSeed(num):
  seedList = []
  for x in range(numtl):
    if isProductSeed(x,num):
      seedList.append(x}
  if len(seedList) == 0:
    print("there are no product seeds”)
  else:
    for x in seedList:
      print(x)


