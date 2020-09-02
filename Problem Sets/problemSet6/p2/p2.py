

def isPrefixString(word, arr):
    comboWord = ""
    
    for x in range(len(arr)):
        comboWord += arr[x]
        if comboWord == word:
            return True
    
    return False
    

def prefixStrings(a, b):
    for word in b:
        if isPrefixString(word, a):
            continue
        else:
            return False
            
    return True
            

