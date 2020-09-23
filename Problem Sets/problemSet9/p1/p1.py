def mergingLetters(s, t):
    finalString = ""
    
    sCounter = 0
    tCounter = 0
    
    for x in range(len(s)+len(t)):
        if tCounter == len(t):
            finalString += s[sCounter]
            sCounter += 1
            continue
        if sCounter == len(s):
            finalString += t[tCounter]
            tCounter += 1
            continue
        
        
        if x%2 == 0:
            finalString += s[sCounter]
            sCounter += 1
        if x%2 == 1:
            finalString += t[tCounter]
            tCounter += 1
        
    return finalString

