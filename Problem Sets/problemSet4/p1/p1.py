#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'compressedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING message as parameter.
#


'''
strat:
loop through message. (len -1 maybe)
if the next one is equal to the current one, then have a counter variable and add to that.

if its different then check:
    is the counter 0 or 1?:
        yes: add the letter
        no: add the counter to the string and reset the counter


'''


def compressedString(message):
    finalString = ""
    counter = 1
    newMessage = message + "-"

    for x in range(len(newMessage)-1):
        if newMessage[x] == newMessage[x+1]:
            counter += 1
        else:
            if counter <= 1:
                finalString += newMessage[x]
            else:
                finalString += newMessage[x] + str(counter)
                counter = 1
    
    return finalString




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