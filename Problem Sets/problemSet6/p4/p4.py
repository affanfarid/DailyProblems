def booleanDeque(n, operations):
    finalString = "0"*n
    for x in operations:
        if x == "L":
            for y in range(len(finalString)):
                if finalString[y] == 0:
                    finalString[y] = 1
                    break
        
        if x[0] == "C":
            num = int(x[1])
            finalString[num] = "0"
            
    return finalString
    #return "0"*n
