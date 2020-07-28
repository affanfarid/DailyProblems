'''
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6

Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42

'''

'''
start at root
have a currMax that gets passed along and edited 

so we have these parties:

the left branch + the current node value + the right branch
the left branch + current node
the right branch + current node 

we can only pass up the left/right branch plus current node, 
NOT both 

but we CAN update the currMax. 
basically use both branches + current to update currMax.
and pass on the greater of current + left/right



'''
class Node:
  def __init__(self, value, left, right):
    self.value = value
    self.left = left
    self.right = right


def maxPathSum(node):
  currMax = [0]
  maxPathSumRec(node, currMax)
  return currMax[0]

def maxPathSumRec(node, currMax):
  #leaf node
  if node.left == None and node.right == None:
    currMax[0] = max(currMax[0], node.value)

    return node.value
  #only has a right node
  if node.left == None and node.right != None:
    rightSum = maxPathSumRec(node.right, currMax)
    currMax[0] = max(currMax[0], rightSum + node.value)

    return rightSum + node.value
  #only has a left node
  if node.left != None and node.right == None:
    leftSum = maxPathSumRec(node.left, currMax)
    currMax[0] = max(currMax[0], leftSum + node.value)

    return leftSum + node.value
  #has both left and right branches
  else:
    leftSum = maxPathSumRec(node.left, currMax)
    rightSum = maxPathSumRec(node.right, currMax)
    currMax[0] = max(currMax[0], leftSum + rightSum + node.value)

    return max(leftSum, rightSum) + node.value



#   1
# 2   3
t1n3 = Node(3, None, None)
t1n2 = Node(2, None, None)
t1n1 = Node(1, t1n2, t1n3 )

#     1
#    / \
#   2   5
#  / \   \
# 3   4   6

t2n6 = Node(6, None, None)
t2n5 = Node(5, None, t2n6)
t2n4 = Node(4, None, None)
t2n3 = Node(3, None, None)
t2n2 = Node(2, t2n3, t2n4)
t2n1 = Node(1, t2n2, t2n5)

#       -1
#    /    \
#   2      5
#  / \   /  \
# 3   4 6    -7

t3n7 = Node(-7, None, None)
t3n6 = Node(6, None, None)
t3n5 = Node(5, t3n6, t3n7)
t3n4 = Node(4, None, None)
t3n3 = Node(3, None, None)
t3n2 = Node(2, t3n3, t3n4)
t3n1 = Node(-1, t3n2, t3n5)

  #  -10
  #  / \
  # 9  20
  #   /  \
  #  15   7


t4n5 = Node(7, None, None)
t4n4 = Node(15, None, None)
t4n3 = Node(20, t4n4, t4n5)
t4n2 = Node(9, None, None)
t4n1 = Node(-10, t4n2, t4n3)

print(maxPathSum(t1n1)) #3
print(maxPathSum(t2n1)) #18
print(maxPathSum(t3n1)) #16
print(maxPathSum(t4n1)) #42

