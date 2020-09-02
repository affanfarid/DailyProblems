'''
strat:
line of stars of width 

line of stars of width

'''

def justifyNewspaperText(lines, aligns, width):
    finalArr = []
    tempArr = []
    
    for x in range(len(lines)):
        tempLine = " ".join(lines[x])
        #if the line already fits in the width
        if len(tempLine) == width:
            tempArr.append(tempLine)
            continue
        #if the line is smaller than the width
        if len(tempLine) < width:
            if aligns[x] == "LEFT":
                tempLine += " "*(width-len(tempLine) )
            if aligns[x] == "RIGHT":
                tempLine = " "*(width-len(tempLine) ) + tempLine
            tempArr.append(tempLine)
            continue
        #line is greater than width
        if len(tempLine) > width:
            ###
            tmp = lines[x]
            counter = 0
            while(counter + 1  < len(tmp) ):
                if len(tmp[counter]) + len(tmp[counter+1]) + 1 <= width:
                    tmp[counter] = " ".join(tmp[counter:counter+2])
                    del tmp[counter+1]
                else:
                    counter += 1
                    
            
            ###
            
            for y in tmp:
                if aligns[x] == "LEFT":
                    y += " "*(width-len(y) )
                if aligns[x] == "RIGHT":
                    y = " "*(width-len(y) ) + y
                tempArr.append(y)
                
        
    
    
    #format at end
    tempArr.insert(0, "*"*width)
    tempArr.append("*"*width)
    for x in tempArr:
        finalLine = "*" + x + "*"
        finalArr.append(finalLine)
        
    return finalArr

