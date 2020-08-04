'''
We are given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.

Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

(Recall that the subtree of a node X is X, plus every node that is a descendant of X.)

Example 1:
Input: [1,null,0,0,1]
Output: [1,null,0,null,1]
 
Explanation: 
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.



Example 2:
Input: [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]



Example 3:
Input: [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]

'''

'''
strat:

start at root node:
-if its none, return true
-if its 0
  - if both left rec and right rec are true
    delete the node
    return true
-if its 1
  -perform the left rec and the right rec
  - return false



'''

class Node:
  def __init__(self, value, left, right):
    self.value = value
    self.right = right
    self.left = left

#shell function (isnt needed i guess)
def binTreePrune(root):
  temp = binTreePruneRec(root)
  return root

#recursive function
def binTreePruneRec(node):
  #if the node is empy, returns True
  if node == None:
    return True
  #if its 0, checks if both the left and right are also "deleteable"
  #if they are, deletes them via recursive calls, and then deletes itself
  if node.value == 0:
    leftBool = binTreePruneRec(node.left)
    rightBool = binTreePruneRec(node.right)
    if leftBool and rightBool:
      #del node
      node.value = "null"
      return True
    #if a 1 is found in the subtree, doesnt do anything and returns False
    #thus "saving" the branch 
    else:
      return False
  #if its 1, then its gonna return false, but checks the subtrees
  if node.value == 1:
    leftBool = binTreePruneRec(node.left)
    rightBool = binTreePruneRec(node.right)
    return False

#for printing
def traverse(rootnode):
  thislevel = [rootnode]
  while thislevel:
    nextlevel = list()
    for n in thislevel:
      print(n.value, end =" ")
      if n.left: 
        nextlevel.append(n.left)
      if n.right: 
        nextlevel.append(n.right)
    print("")
    thislevel = nextlevel

#for testing
def testNode(node):
  print("Before:")
  traverse(node)
  print("------")
  binTreePrune(node)
  traverse(node)
  print("Done")

#   1
# 0   0
t1n3 = Node(0, None, None)
t1n2 = Node(0, None, None)
t1n1 = Node(1, t1n2, t1n3 )

#     1
#    / \
#   0   0
#  / \   \
# 0   0   1

t2n6 = Node(1, None, None)
t2n5 = Node(0, None, t2n6)
t2n4 = Node(0, None, None)
t2n3 = Node(0, None, None)
t2n2 = Node(0, t2n3, t2n4)
t2n1 = Node(1, t2n2, t2n5)

#      0
#    /    \
#   0      0
#  / \   /  \
# 0   1 1    1

t3n7 = Node(1, None, None)
t3n6 = Node(1, None, None)
t3n5 = Node(0, t3n6, t3n7)
t3n4 = Node(1, None, None)
t3n3 = Node(0, None, None)
t3n2 = Node(0, t3n3, t3n4)
t3n1 = Node(0, t3n2, t3n5)

  #   0
  #  / \
  # 0  0
  #   /  \
  #  0   0


t4n5 = Node(0, None, None)
t4n4 = Node(0, None, None)
t4n3 = Node(0, t4n4, t4n5)
t4n2 = Node(0, None, None)
t4n1 = Node(0, t4n2, t4n3)

testNode(t1n1)
testNode(t2n1)
testNode(t3n1)
testNode(t4n1)
