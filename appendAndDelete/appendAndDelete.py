def appendAndDelete(s,t,k):
    sNum = len(s)
    totalNum = 0
    for x in range(len(s)):
        if s[:x] in t:
            continue
        else:
            sNum = x - 1
            break
    #totalNum += len(s) - sNum
    print(s[:sNum])
    t = t.replace(s[:sNum],'')
    print(t)
    totalNum = len(t) + len(s) - sNum

    print(totalNum)
    return totalNum == k


s1 = "hackerhappy"
t1 = "hackerrank"
print(appendAndDelete(s1, t1, 9))

s2 = "hacker"
t2 = "hackerrank"
print(appendAndDelete(s2, t2, 4))