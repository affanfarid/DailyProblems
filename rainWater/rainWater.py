'''

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 8



'''


'''
strat:
-no recursion
-loop through once
-layer by layer?????????

-pool toggle?
-current pool height
-total volume


pool toggle off
loop:
-is the next index value higher?
  -yes,
    -if the pool toggle is on 
      -total volume+= pool height - current height

SCRAPPED




---

strat2:
start from the first non zero value
ending and starting dont count for "pool" measuring


loop through the array
take value. if the value after it is less than the value
-you know theres a pool, OR it reaches the end
-search the rest of the array (after current position) for something of equal or greater value
SCRAPPED

--

Strat 3:
dict that carries all potential volumes, and then "dumps" them once its
confirmed its a "pool"

'''


def rainVolume(arr):

  volume = 0
  tempDict = {level: 0 for level in range( max(arr) + 1 ) } 
  currPoolLevel = arr[0]
  currPoolMax = arr[0]
    
  
  for x in arr:
    print("level= "+ str(x))
    
    #currPoolMax = max(currPoolLevel, x)
    if x > currPoolMax:
      for y in range(0,currPoolMax):
        volume += tempDict[y]
        tempDict[y] = 0
      #end with this
      print("Max change. Dumping all.")
      currPoolMax = x
      

    #slope goes "down"
    if x <= currPoolLevel:
      for y in range(x,currPoolMax):
        print("added 1 going down")
        tempDict[y] += 1

    #slope goes "up"
    if x > currPoolLevel:
      for y in range(0,x):
        print("cleared dump: " + str(y))
        volume += tempDict[y]
        tempDict[y] = 0

      if x < currPoolMax:
        for z in range(x,currPoolMax):
          tempDict[z] += 1
      #add if statement for extra stuff


    #at the end
    print(tempDict)
    print("Volume is: " +str(volume))
    print("----")
    currPoolLevel = x

  return volume

    
test1 = [3,2,1,0,2,4] #return 7
test2 = [3,2,1,0,2,4,2,2,3] # return 9
test3 = [0,1,0,2,1,0,1,3,2,1,2,1] #return 6
test4 = []
test5 = []

print(rainVolume(test1))
