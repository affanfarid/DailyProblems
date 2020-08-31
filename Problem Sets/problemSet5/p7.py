#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'funWithAnagrams' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY text as parameter.
#
'''
given a list of words. return an ordered list of words, where only the first word of an anagram is kept.

aka if theres "code" and "doce", if code comes first, remove doce but keep code. 

'''

def funWithAnagrams(text):
    finalList = []
    sortedWordDict = {}

    for x in text:
        sortWord = str(sorted(x))
        if sortWord not in sortedWordDict:
            finalList.append(x)
            sortedWordDict[sortWord] = True
        
    return sorted(finalList)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    text_count = int(input().strip())

    text = []

    for _ in range(text_count):
        text_item = input()
        text.append(text_item)

    result = funWithAnagrams(text)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
