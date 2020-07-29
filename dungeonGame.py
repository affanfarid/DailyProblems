'''

The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

 

Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2(K) 	-3 	  3
-5 	   -10 	  1
10 	    30   -5(P)

 

Note:

    The knight's health has no upper bound.
    Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

'''


'''
strat:
first focus on traversal
going to have a recursive traversal

at the end, return the sum aka pass the sum along?
---
[3,4,-10,8,-1,-2]
starting is 0.
add 3 cause its positive. thats ok.
same with 4. now we have 7.
-10 is negative, so add 3 to minHealth.

reset back at 0 health for the next one.
its 8, so health is 8.
-1 is 7, still ok,
-2 is 5, still ok.

minhealth is 3 + 1. 

start at a tile. with minHealth as 0
if the tile+ minHealth is less than or equal to 0
  - add the tile value to 

---

ACTUAL STRAT:
minHealth = 0; this is the minimum amount of health required
health = 0; this is your current health.

start at tile
if the tile is less than the current health + tile amount (meaning it dips to where the player dies)
  then add the difference between the current health and the tile to keep the player barely alive
  also reset the health to 0 because its as if you took away the health and then gave enough to keep the player alive.
otherwise then just add the tile amount to health

The goal is to see how much you GIVE the player to keep him alive

then pass in health and minhealth for both the right and down tiles, aka recursively.


'''

def dungeonGame(arr):
  return dungeonGameRec(arr,0,0,0,0)

def dungeonGameRec(arr,x,y,health, minHealth):
  #print("tile: " + str(arr[x][y]))

  #if the tile's addition kills the player, then and the minimum amount to keep him alive
  if arr[x][y] + health < health:
    minHealth += abs(health + arr[x][y])
    #reset health to 0 to simulate him barely alive
    health = 0
  else:
    #otherwise just increase the health
    health += arr[x][y]
    
  #print("minhealth: "+ str(minHealth))

  #reached princess
  if x == len(arr)-1 and y == len(arr[0])-1:
    #print("minHealthFinal: " + str(minHealth))

    #add one because health cant be 0 at any time.
    return minHealth + 1 
  #on bottom edge, can only move right
  elif x == len(arr)-1: 
    return dungeonGameRec(arr,x,y+1,health, minHealth)
  #on right edge, can only move down
  elif y == len(arr[0])-1:  
    return dungeonGameRec(arr,x+1,y,health, minHealth)
  #has the option to move both down or right
  else:
    #return the minimum of the two paths
    return min(
                dungeonGameRec(arr,x,y+1,health, minHealth ),
                dungeonGameRec(arr,x+1,y,health, minHealth )
              )


test1 = [
  [-2,-3,3],
  [-5,-10,1],
  [10,30,-5]

]

test2 = [
  [-5,-3],
  [-2,7]
]

test3 = [
  [-31]
]

test4 = [
  [-10,1],
  [30,-5]
]

print(dungeonGame(test1))
print(dungeonGame(test2))
print(dungeonGame(test3))
print(dungeonGame(test4))
