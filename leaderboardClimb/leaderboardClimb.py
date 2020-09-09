import math
import os
import random
import re
import sys

def getRank(scoreSet, score):
    if score in scoreSet:
        return scoreSet.index(score) + 1
    else:
        for x in range(len(scoreSet)):
            if score > scoreSet[x]:
                scoreSet.insert(x,score)
                return x+1
        scoreSet.append(score)
        return len(scoreSet)


# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    finalList = []
    scoreSet = list(set(scores))
    scoreSet.sort(reverse=True)

    for x in alice:
        finalList.append(getRank(scoreSet, x))
        
    return finalList

scores1 = [100, 100, 50, 40, 40, 20, 10]
alice1 = [5, 25, 50, 120]
print(climbingLeaderboard(scores1, alice1)) #[6,4,2,1]