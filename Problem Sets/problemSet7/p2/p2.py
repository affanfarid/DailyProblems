# Sample code to read input and write output:

'''
NAME = raw_input()            # Read input from STDIN
print 'Hello %s' % NAME       # Write output to STDOUT
'''

# Warning: Printing unwanted or ill-formatted 
# data to output will cause the test cases to fail

# Write your code here



def isPrime(num):
    if (num <= 1):
        return False
    if (num <=3):
        return True
    
    if (num % 2 == 0 or num %3 == 0):
        return False
    
    i = 5
    while (i * i <= num):
        if( num % i == 0 or num % (i+2) == 0):
            return False
        i += 6
    return True



def prob2():

    
    contents = []
    while True:
        try:
            line = raw_input("")
        except EOFError:
            break
        contents.append(line)
        
    strArr = contents[1].split(" ")
    arr = []
    for x in strArr:
        arr.append(int(x))
        
        
    finalString = ""
    for x in arr:
        if isPrime(x):
            finalString += "Prime "
        else:
            finalString += "Composite "
    
    print(finalString)
    
    #return finalString
    
    
prob2()
        

        
        
        
        
        
        
        