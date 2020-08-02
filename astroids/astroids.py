'''
 We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example 1:

Input: 
asteroids = [5, 10, -5]
Output: [5, 10]
Explanation: 
The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.

Example 2:

Input: 
asteroids = [8, -8]
Output: []
Explanation: 
The 8 and -8 collide exploding each other.

Example 3:

Input: 
asteroids = [10, 2, -5]
Output: [10]
Explanation: 
The 2 and -5 collide resulting in -5.  The 10 and -5 collide resulting in 10.

Example 4:

Input: 
asteroids = [-2, -1, 1, 2]
Output: [-2, -1, 1, 2]
Explanation: 
The -2 and -1 are moving left, while the 1 and 2 are moving right.
Asteroids moving the same direction never meet, so no asteroids will meet each other.


'''

'''
[3,5,-8,9,-7]

first compare 3 and 5. they are both positive, so nothing happens.
then compare 5 and -8. they are different signs
> -8 overpowers 5. so 5 gets deleted. 
now compare -8 to 3.
> -8 overpowers 3, so 3 gets deleted.
-8 is now the first element in the array. it rests there.
Now compare -8 to 9. they are opposite signs but are going in diff directions.
both are kept.
now compare 9 to -7.
> 9 overpowers -7. -7 gets deleted. 
theres nothing left, so we are done.

strat:
-have two running indecies which get updated.
-have several if statements comparing the numbers
 - two positives
 - two negatives
 (two positives and two negatives can be done by multiplying and seeing if they result in a positive product)
 -if the product isnt negative, then compare the positions.

'''

#O(n) solution
def astroids(arr):
  x = 0
  #this is the max x can go to by default, which is len(arr)-2 because
  #the comparison includes arr[x+1]
  arrLen = len(arr)-2

  while(x<=arrLen):
    # print("x: "+ str(x))
    # print("comparing: {0} and {1}".format(arr[x],arr[x+1]))

    #compare arr[x] with arr[x+1]
    #they are different signs
    if arr[x]*arr[x+1] < 0:
      #negative is on right; if negative on left, nothing happens
      if arr[x] >= 0:
        #positive is greater in value
        if abs(arr[x]) > abs(arr[x+1]):
          #delete it, and decrease the index by 2:
          #one to compensate the deletion
          #and one for the extra comparison to "percolate" the negative astroid back
          del arr[x+1]
          x -= 2
          arrLen -= 1
        #negative is greater in value
        elif abs(arr[x]) < abs(arr[x+1]):
          del arr[x]
          x -= 2
          arrLen -= 1
        #they are equal in value
        else:
          del arr[x-1]
          del arr[x]
          x -= 2
          arrLen -= 2
    x += 1

  return arr

# test1 = [3,5,-8,9,-7]
# test2 = [-2,-1,1,2]
# test3 = [1,2,3,4,5,6,7,-8]
#test4 = [8,1,2,3,4,5,6,7,-8]
# test5 = [8,1,-8]
#print(astroids(test4))
          



