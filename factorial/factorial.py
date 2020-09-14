#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    retVal = n
    for x in range(1,n):
        retVal *= x
    print(retVal)
    return retVal

if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)

