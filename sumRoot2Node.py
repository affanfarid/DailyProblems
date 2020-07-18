'''
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Example 2:

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.



'''


'''
[4,9,0,5,1]
 1,2,3,4,5
index starts at 1 lets say
the leaves of a node are index*2 and (index*2)+1

      5
    /  \
  3     8
       /\
      1  2

[0,5,3,8,N,N,1,2]
[0,1,2,3,4,5,6,7]

strat:
-recursive
-pass the string along
-if both left and right are Null, then convert string to num and add to array
'''

class Node:
  def __init__(self, value, left, right):
    self.value = value
    self.left = left
    self.right = right


def sumR2L(root):
  sumArr = []
  sumR2LRec(root, sumArr, "" )
  return sum(sumArr)

def sumR2LRec(node, sumArr, numStr):
  #node left and node right are out of bounds
  if node.right == None and node.left == None:
    sumArr.append( int(numStr+str(node.value)) ) 
    return
  elif node.right == None:
    sumR2LRec(node.left, sumArr, numStr+str(node.value))
  elif node.left == None:
    sumR2LRec(node.right, sumArr, numStr+str(node.value))
  else:
    sumR2LRec(node.left, sumArr, numStr+str(node.value))
    sumR2LRec(node.right, sumArr, numStr+str(node.value))
  

  
  #   1
  #  / \
  # 2   3

r1n1 = Node(2, None, None)
r1n2 = Node(3, None, None)
root1 = Node(1, r1n1, r1n2)

#     4
#    / \
#   9   0
#  / \
# 5   1

r2n4 = Node(1, None, None)
r2n3 = Node(5, None, None)
r2n1 = Node(9, r2n3, r2n4)
r2n2 = Node(0, None, None)
root2 = Node(4, r2n1, r2n2)


  #     5
  #   /  \
  # 3     8
  #      /\
  #     1  2
      #  /
      # 5

r3n5 = Node(5, None, None)
r3n4 = Node(1, r3n5, None)
r3n3 = Node(2, None, None)
r3n2 = Node(8, r3n4, r3n3)
r3n1 = Node(3, None, None)
root3 = Node(5, r3n1, r3n2)

print(sumR2L(root1)) #25
print(sumR2L(root2)) #1026
print(sumR2L(root3)) #6450

  
  
