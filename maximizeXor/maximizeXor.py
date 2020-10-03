def maximizeXor(l,r):
    maxXor = 0
    for x in range(l,r+1):
        for y in range(x,r+1):
            num1 = bin(x)
            num2 = bin(y)
            binNum = bin(num1 ^ num2)
            xorVal = int(binNum,2)
            maxXor = max(maxXor, xorVal)

    return maxXor

