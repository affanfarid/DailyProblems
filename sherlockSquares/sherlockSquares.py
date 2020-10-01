import math

def sherlockSquares(a, b):
    numList = range(a,b+1)
    count = 0
    for x in range(int(math.sqrt(a-1)), int(math.sqrt(b+1))+1 ):
        if x*x > b:
            break
        if x*x in numList:
            count += 1

    return count


print(sherlockSquares(24,49))
print(sherlockSquares(17,24))
