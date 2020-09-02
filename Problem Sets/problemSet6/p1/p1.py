def countArithmeticMeans(a):
    finalNum = 0
    
    if len(a) == 0:
        return 0
    if len(a) == 1:
        if a[0] == 0:
            return 1
        else:
            return 0
    
    
    for x in range(len(a)):
        if x==0:
            if a[x] == (a[x+1] + 0 )/2:
                finalNum += 1
        elif x== len(a)-1:
            if a[x] == (a[x-1] + 0 )/2:
                finalNum += 1
        else:
            if a[x] == (a[x-1] + a[x+1])/2:
                finalNum += 1
                
    return finalNum