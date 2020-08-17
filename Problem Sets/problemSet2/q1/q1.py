'''
strat:
first entry in arr has to be 1. 
sort the array first. 
reduce the first entry of the sorted array to 1. 

for the rest, make sure the entry is within one of the previous entry
if its not, reduce it so it is 1

'''

def getMaxValue(numGroups, arr):
    #sort list in ascending order
    temp = arr
    temp.sort()
    #make sure the first group has exactly 1
    arr[0] = 1
    

    for x in range(1,len(temp)):
        #check if the group has a difference more than 1 to the previous group
        if temp[x] - temp[x-1] > 1:
            #if it does, reduce the group to the previous group value +1 because we are maximizing
            temp[x] = temp[x-1] + 1
    
    #return the last element of the array 
    return temp[-1]
    
