'''
In a warehouse, there is a row of barcodes, where the i-th barcode is barcodes[i].

Rearrange the barcodes so that no two adjacent barcodes are equal.  You may return any answer, and it is guaranteed an answer exists.

 

Example 1:

Input: [1,1,1,2,2,2]
Output: [2,1,2,1,2,1]

Example 2:

Input: [1,1,1,1,2,2,3,3]
Output: [1,3,1,3,2,1,2,1]


'''


'''
strat:
analyze indecies i and i+1.
if they are different, then move on.
if they are the same, then loop through the rest of the array to find a different one.
once a different one is found, swap it with i+1. 
if you go through the rest of the array and its not found, start the beginning and go up until i
swap only if the surrounding ones are not equal to index i


'''

def distantBarcode(arr):
    newArr = arr
    #loops through array 
    for i in range(len(newArr)-1):

        if newArr[i] != newArr[i+1]:
            continue
        else:
            
            flag = True

            #searches rest of array AHEAD of index for a valid number to swap
            for j in range(i+1, len(newArr) ):
                #print(f"i+1: {arr[i+1]}; j: {arr[j]}")

                #if its not equal, swap em
                if newArr[i+1] != newArr[j]:

                    newArr[i+1], newArr[j] = newArr[j], newArr[i+1]
                    flag = False
                    break
            
            #if no available swap is found AHEAD of the index, seach the rest of the array BEHIND index
            if flag:
                for k in range(len(newArr[:i+1])):
                    #cant check space behind index if index is 0
                    if k == 0:
                        #searches for index where surrounding spots are not equal to the one we are trying to swap
                        if newArr[k] != newArr[i+1] and newArr[k+1] != newArr[i+1]:
                            #swap em and break
                            newArr[i+1], newArr[k] = newArr[k], newArr[i+1]
                            break
                    else:
                        #same thing as above but checks behind as well 
                        if newArr[k] != newArr[i+1] and newArr[k+1] != newArr[i+1] and newArr[k-1] != newArr[i+1]:
                            newArr[i+1], newArr[k] = newArr[k], newArr[i+1]
                            break

            
        


    return newArr



print(distantBarcode([1,1,1,2,2,2]))
print(distantBarcode([1,1,1,1,2,2,3,3]))
print(distantBarcode([1,1,2,2,2,2,3,3,3,3]))
print(distantBarcode([3,3,3,3,2,2,2,2,1,1]))
print(distantBarcode([1,2,1,2,1,2,1,2,1]))