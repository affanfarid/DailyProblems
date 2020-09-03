# Sample code to read input and write output:

'''
NAME = input()                # Read input from STDIN
print("Hello " + NAME)        # Write output to STDOUT
'''

# Warning: Printing unwanted or ill-formatted 
# data to output will cause the test cases to fail

# Write your code here


def problem3():
    
    line = input()
    numCombos = [0]
    problem3Rec(line, numCombos)
    return numCombos[0]
    
    
    
def problem3Rec(arr, numCombos):
    if len(arr) == 0:
        numCombos[0] += 1
    elif len(arr) >= 2:
            if int(arr[0]) == 2 and int(arr[1]) <= 6:
                problem3Rec(arr[1:],numCombos)
                problem3Rec(arr[2:],numCombos)
            elif int(arr[0]) == 1:
                problem3Rec(arr[1:],numCombos)
                problem3Rec(arr[2:],numCombos)
            else:
                problem3Rec(arr[1:],numCombos)
    else:
        problem3Rec(arr[1:],numCombos)
                
        
    
    
x = problem3()
print(x)