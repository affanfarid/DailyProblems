import sys
text = "".join(sys.stdin.readlines())
# print(text)


def func1(n):
    temp = ""
    for x in range(n):
        temp += str(n) + " "
        
    print(temp)
    
    temp = ""
    counter = 1
    for y in range(n):
        for x in range(n):
            if x == n -2:
                temp += str(counter) + " "
            else:
                temp += str(n) + " "
            
        counter += 1
        print(temp)
        temp = ""
            
                


func1(int(text))