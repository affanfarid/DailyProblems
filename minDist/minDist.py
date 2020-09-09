#!/bin/python3

import math
import os
import random
import re
import sys



'''
strat:

'''


def minDist(b):
    minNum = 9999
    for x in range(len(b)-1):
        minNum = min(minNum, b[x+1]-b[x] )
    return minNum


def minimumDistances(a):
    distDict = {}
    minNum = 9999
    for x in range(len(a)):
        num = a[x]
        if num not in distDict:
            distDict[num] = [x]
        else:
            distDict[num].append(x)
    
    for y in distDict:
        #print(distDict[y])
        if len(distDict[y]) <= 1:
            continue
        minNum = min(minNum, minDist(distDict[y]))

    if minNum == 9999:
        return -1
    else:
        return minNum


test1 = [3,2,1,2,3]
print(minimumDistances(test1))
    


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input())

#     a = list(map(int, input().rstrip().split()))

#     result = minimumDistances(a)

#     fptr.write(str(result) + '\n')

#     fptr.close()
