

def equallyRearranging(str1):
    outputStr = ""
    
    cycleStr = "WDL"
    
    while str1 != "":
        temp = cycleStr[0]
        # print(temp)
        # print(str1)
        if temp in str1:
            outputStr += temp
            str1 = str1.replace(temp,"",1)
        cycleStr = cycleStr[1:] + temp

    
    return outputStr
              
    
        

