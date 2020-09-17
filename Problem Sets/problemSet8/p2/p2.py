#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'prison' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER_ARRAY h
#  4. INTEGER_ARRAY v
#

def diff(list1, list2):
    return (list(list(set(list1)-set(list2)) + list(set(list2)-set(list1))))

def prison(n, m, h, v):
    barsH = [x for x in range(n+1)]
    barsV = [x for x in range(m+1)]
    barsH = diff(barsH, h)
    barsV = diff(barsV, v)



    gapH = 0
    gapV = 0

    barsH.sort()
    barsH.append(n+1)
    barsV.sort()
    barsV.append(m+1)
    for b in range(len(barsH)-1):
        tempGap = barsH[b+1] - barsH[b]
        if tempGap > gapH:
            gapH = tempGap
    for b in range(len(barsV)-1):
        tempGap = barsV[b+1] - barsV[b]
        if tempGap > gapV:
            gapV = tempGap

    return gapH * gapV
    

