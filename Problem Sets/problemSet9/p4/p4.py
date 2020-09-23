
def rectangleBoxes(operations):
    saved = []
    boolArr = []
    #print(operations)
    for x in operations:
        #print(x)
        if type(x) is not list: 
            continue
        if x[0] == 0:
            temp = [x[1],x[2]]
            saved.append(temp)
        if x[0] == 1:
            a = x[1]
            b = x[2]
            
            tempBool = True
            for rec in saved:
                if rec[0] <= a and rec[1] <= b:
                    tempBool = True and tempBool
                elif rec[0] <= b and rec[1] <= a:
                    tempBool = True and tempBool
                else:
                    tempBool = False and tempBool
            boolArr.append(tempBool)
    return boolArr