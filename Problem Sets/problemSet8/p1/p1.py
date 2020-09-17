#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'efficientJanitor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts FLOAT_ARRAY weight as parameter.
#


'''
loop through, for the first one

'''
def efficientJanitor(weight):

    weight.sort()
    left = 0
    right = len(weight) -1
    count = 0
    while(left<=right):
        if left == right:
            count += 1
            break
        if weight[left] + weight[right] <= 3.0:
            left += 1
            right -= 1
            count += 1
        else:
            right -= 1
            count += 1
    
    return count


