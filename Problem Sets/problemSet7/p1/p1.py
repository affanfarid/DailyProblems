# Sample code to read input and write output:

'''
NAME = input()                # Read input from STDIN
print("Hello " + NAME)        # Write output to STDOUT
'''

# Warning: Printing unwanted or ill-formatted 
# data to output will cause the test cases to fail

# Write your code here


def problem1():
    # i1 = input()
    # # for x in range(2):
    # #     i1 += input()
    # print(i1)
    
    contents = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        contents.append(line)
    
    #print(contents)
    strArr = contents[1].split(" ")
    arr = []
    for x in strArr:
        arr.append(int(x))

    
    # arr = []
    mean = sum(arr)/len(arr)
    mode = max(set(arr), key=arr.count)
    
    
    mean4digit = "{:.4f}".format(mean)
    
    finalString = str(mean4digit) + " " + str(mode)
    print(finalString)
    
problem1()
        
    