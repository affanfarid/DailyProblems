#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'deviceNamesSystem' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY devicenames as parameter.
#

def deviceNamesSystem(devicenames):
    deviceDict = {}
    finalNames = []

    for x in devicenames:
        if x not in deviceDict:
            deviceDict[x] = 1
        else:
            num = deviceDict[x]
            deviceDict[x] += 1
            x += str(num)
        finalNames.append(x)
    
    return finalNames


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    devicenames_count = int(input().strip())

    devicenames = []

    for _ in range(devicenames_count):
        devicenames_item = input()
        devicenames.append(devicenames_item)

    result = deviceNamesSystem(devicenames)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
