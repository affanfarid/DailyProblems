'''
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

 

Example 1:

Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:

Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

Example 3:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.

 

Constraints:

    The number of nodes in the binary tree is in the range [1, 10^5].
    Each node's value is between [-10^4, 10^4].


'''
class Node:
  def __init__(self,value,left,right):
    self.value = value
    self.left = left
    self.right = right


def goodNodes(root):
  return goodNodesRec(root,0)

def goodNodesRec(node,currMax):
  retVal = 0
  if node.value >= currMax:
    retVal = 1

  if node.left == None and node.right == None:
    return retVal
  elif node.left == None:
    return retVal + goodNodesRec(node.right, max(currMax,node.value))
  elif node.right == None:
    return retVal + goodNodesRec(node.left, max(currMax,node.value))
  else:
    return retVal + goodNodesRec(node.right,max(currMax, node.value)) + goodNodesRec(node.left, max(currMax, node.value))



#   1
# 2   1
t1n3 = Node(1, None, None)
t1n2 = Node(2, None, None)
t1n1 = Node(1, t1n2, t1n3 )

#     3
#    / \
#   4   1
#  / \   \
# 1   5   3

t2n6 = Node(3, None, None)
t2n5 = Node(1, None, t2n6)
t2n4 = Node(5, None, None)
t2n3 = Node(1, None, None)
t2n2 = Node(4, t2n3, t2n4)
t2n1 = Node(3, t2n2, t2n5)

#      3
#    /    \
#   5      1
#  / \   /  \
# 6   4 3    2

t3n7 = Node(2, None, None)
t3n6 = Node(3, None, None)
t3n5 = Node(1, t3n6, t3n7)
t3n4 = Node(4, None, None)
t3n3 = Node(6, None, None)
t3n2 = Node(5, t3n3, t3n4)
t3n1 = Node(3, t3n2, t3n5)

  #   3
  #  # \
  # #  3
  #   /  \
  #  4   2


t4n5 = Node(2, None, None)
t4n4 = Node(4, None, None)
t4n3 = Node(3, t4n4, t4n5)
#t4n2 = Node(0, None, None)
t4n1 = Node(3, None, t4n3)

#t1 3
# t2 4
#t3 4
#t4 3

print(goodNodes(t1n1)) #3
print(goodNodes(t2n1)) #4
print(goodNodes(t3n1)) #4
print(goodNodes(t4n1)) #3


