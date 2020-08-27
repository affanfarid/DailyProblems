#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getNumberOfOptions' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY priceOfJeans
#  2. INTEGER_ARRAY priceOfShoes
#  3. INTEGER_ARRAY priceOfSkirts
#  4. INTEGER_ARRAY priceOfTops
#  5. INTEGER budgeted
#

'''
strat:
go recursive and loop through each one. 

'''


def getNumberOfOptions(priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops, budgeted):
    comboArr = [0]
    jeansRec(priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops, budgeted, comboArr)
    return comboArr[0]

def jeansRec(jeansArr, shoesArr, skirtsArr, topsArr, budget, comboArr):
    for x in jeansArr:
        if budget - x > 0:
            shoesRec(shoesArr, skirtsArr, topsArr, budget - x, comboArr)


def shoesRec(shoesArr, skirtsArr, topsArr, budget, comboArr):
    for x in shoesArr:
        if budget - x > 0:
            skirtsRec(skirtsArr, topsArr, budget - x, comboArr)


def skirtsRec(skirtsArr, topsArr, budget, comboArr):
    for x in skirtsArr:
        if budget - x > 0:
            topsRec(topsArr, budget - x, comboArr)


def topsRec(topsArr, budget, comboArr):
    for x in topsArr:
        if budget - x >= 0:
            comboArr[0] += 1




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