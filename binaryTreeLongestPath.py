'''
Problem: Given the root node of a binary tree, return the length of the longest path in the tree (node to node)

ex. 

      10
    1   20
  0  2

Ex.

                10
              /   \
            4      11
          /  \
        3     5
      /        \
    2           9
  /            /
1             7


Longest path is (1-2-3-4-5-9-7) of length 7

'''


'''
base node
if left and right are null, 
  return 1
else
  return (look at left node), (look at right one) and add 1

  return max ()

10
returns 1 + 

strat:

recursively
somehow pass 


left branch greatest length


---------

def rec(node,highest):
  if node.left and node.right are both null:
    highest = max(highest, 1)
    return 1
  
  elif node.left == None and node.right != None:
    rightVal = rec(node.right, highest)
    highest = max(highest, rightVal+1)
    return rightVal+1

  elif node.left != None and node.right == None:
    rightVal = rec(node.right, highest)
    highest = max(highest, rightVal+1)
    return rightVal+1

  else:
    leftVal = rec(node.left, highest)
    rightVal = rec(node.right, highest)

    highest = max(highest, leftVal+rightVal+1)

    return max(leftVal+1, rightVal+1)



def shellFunc(root):
  highest = 0
  rec(root, highest)

  return highest


'''



def longestPath(root):
  return 
