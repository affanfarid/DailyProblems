def maximizeXor(l,r):
    maxXor = 0
    for x in range(l,r+1):
        for y in range(x,r+1):
            num1 = '0b' + bin(x)
            num2 = '0b' + bin(y)
            binNum = bin(bin(x) ^ bin(y))
            xorVal = int(binNum,2)
            maxXor = max(maxXor, xorVal)

    return maxXor

print(maximizeXor(11,100))
