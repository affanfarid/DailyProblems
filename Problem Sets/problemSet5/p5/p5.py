#problem 5

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'minNum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER samDaily
#  2. INTEGER kellyDaily
#  3. INTEGER difference
#

def minNum(samDaily, kellyDaily, difference):
    samNum = difference
    kellyNum = 0
    numDays = 0
    if difference >= 0 and samDaily >= kellyDaily:
        return -1
    else:
        while (kellyNum <= samNum):
            samNum += samDaily
            kellyNum += kellyDaily
            numDays += 1
        
        return numDays

    # Write your code here





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    samDaily = int(input().strip())

    kellyDaily = int(input().strip())

    difference = int(input().strip())

    result = minNum(samDaily, kellyDaily, difference)

    fptr.write(str(result) + '\n')

    fptr.close()
