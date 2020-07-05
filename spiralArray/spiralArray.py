
'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


'''


'''
strat:

top row, then right column 
invert the array
-flip array 180 degrees

recursive 


'''
def spiralArray(arr):
  outputList = []
  return spiralArrayRec(arr,outputList)
  


def invert2dArray(arr):
  newArr = []
  arr = arr[::-1]
  for x in arr:
    x = x[::-1]
    newArr.append(x)

  return newArr

def spiralArrayRec(arr, outputList):
  

  height = len(arr)
  width = len(arr[0])


  #print top row
  for x in arr[0]:
    outputList.append(x)

  #deletes top row
  arr.remove(arr[0])

  
  #print right column
  if len(arr) > 0:
    for a in range(0,height-1):
      outputList.append(arr[ a ][-1] )

      #deletes last element of row
      arr[a].remove(arr[a][-1])
  

  
  #check if end condition.
  if len(arr) == 0:
    return outputList
  else:
    #pass in the inverted array
    return spiralArrayRec(invert2dArray(arr), outputList)

  #invert the array
    



test1 = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

test2 = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]

print(spiralArray(test1))
print(spiralArray(test2))
#invert2dArray(test1)
#print(invert2dArray(test1))
