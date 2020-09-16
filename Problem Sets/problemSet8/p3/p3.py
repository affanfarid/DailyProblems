#!/bin/python3

import math
import os
import random
import re
import sys




#
# Complete the 'findMinDistance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER w
#  2. INTEGER h
#  3. INTEGER n
#
import itertools
from collections import deque

def findMinDistance(w, h, n):
    arr = []
    ans = float("inf")
    for i in range(h):
        for j in range(w):
            arr.append((i,j,0))

    
    for points in itertools.combinations(arr,n):
        q = deque([]); visited = set()
        for m, n, dist in points:
            q.append((m,n,dist))
            visited.add((m,n))
        distAns = 0
        distArr = []
        while q:
            i, j, dist = q.popleft()
            distAns = max(dist, distAns)
            for x, y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                if 0<=x<h and 0<=y<w and (x,y) not in visited:
                    q.append((x,y,dist+1))
                    visited.add((x,y))
        ans = min(distAns, ans)

    return ans

if __name__ == '__main__':