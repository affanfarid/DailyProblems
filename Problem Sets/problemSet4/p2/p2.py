#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'minMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

'''
strat:
have a function to get minSwaps to sort a binary array.
then check input array to see if more 1s are on left or right
    if more 1s on left, then its easier to push the 1s to the right
        reverse all the 1s and 0s and then return the function of the reverse array
    otherwise (more 1s on right):
        just pass in the original array to the function and return the output

'''

def minMoves(arr):
    mid = len(arr)//2
    #more 1s on the right side
    if sum(arr[:mid]) < sum(arr[mid:]) :
        return minSwaps(arr)
    #more 1s on the left side
    else:
        #flip all 1s and 0s and return minSwaps of the reverse array
        reverseArr = [0 if x==1 else 1 for x in arr]
        return minSwaps(reverseArr)


#returns the minimum swaps to sort a binary array (aka 0s first only)
def minSwaps(arr):
    length = len(arr)
    #stores the count of 0s
    numZeroes = [0] * length
    count = 0

    #count the number of 0s on the right side
    numZeroes[length-1] = 1 - arr[length-1]
    for x in range(length-2, -1, -1):
        #swap
        numZeroes[x] = numZeroes[x+1]
        if (arr[x] == 0):
            numZeroes[x] = numZeroes[x] + 1
    
    #counts the number of swaps by adding number of 0s on the right hand side of each 1
    for y in range(0, length):
        if arr[y] == 1:
            count += numZeroes[y]

    return count

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = minMoves(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
