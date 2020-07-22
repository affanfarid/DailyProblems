'''
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6

The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6


  1
2   3

1
  2
    3

'''


'''
example:
  1
2   3

temp is 3


'''
class Node:
  def __init__(self, value, left, right):
    self.value = value
    self.right = right
    self.left = left


def flatTree(node):
  flatTreeRec(node, None)
  return

def flatTreeRec(node, extra):
  if node.right == None and node.left == None:
    node.right = extra
    return node
  elif node.right == None:
    #TODO
    node.right = flatTreeRec(node.right, extra)
    return
  elif node.left == None:
    #TODO
    node.right = flatTreeRec(node.left, extra)
    return
  #both left and right have values
  else:
    temp = node.right
    node.right = flatTreeRec(node.left, temp)
    node.left = None
    
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

traverse(t2n1)
print("------")
flatTree(t2n1)
traverse(t2n1)
