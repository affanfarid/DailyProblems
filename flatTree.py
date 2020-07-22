

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
  flatTreeRec2(node, None)
  return

#WRONG
def flatTreeRec(node, extra):
  if node.right == None and node.left == None:
    node.right = extra
    return node
  elif node.right == None:
    #TODO
    node.right = flatTreeRec(node.right, extra)
    return node
  elif node.left == None:
    #TODO
    node.right = flatTreeRec(node.left, extra)
    return node
  #both left and right have values
  else:
    #temp = flatTreeRec(node.right, extra)
    temp = node.right 
    node.right = flatTreeRec(node.left, temp)
    node.left = None
    return node


#Right one!
def flatTreeRec2(node, extra):
  #print("on node: "+ str(node.value))
  if node.right == None and node.left == None:
    node.right = extra
    return node
  elif node.right == None:
    node.right = flatTreeRec2(node.left,extra)
    node.left = None
    return node
  elif node.left == None:
    node.right = flatTreeRec2(node.right, extra)
    return node
  #both left and right have values
  else:
    #sort left
    l = flatTreeRec2(node.left, extra)
    #sort right
    #temp = right
    temp = flatTreeRec2(node.right, extra)
    #right = left
    node.right = l
    #left = None
    node.left = None
    #go all the way to bottom of right and add temp to it
    tempNode = node
    while(True):
      #print("node.right is: "+ str(tempNode.right) )
      if tempNode.right == None:
        tempNode.right = temp
        break
      tempNode = tempNode.right
  
    return node
    
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

def testNode(node):
  print("Before:")
  traverse(node)
  print("------")
  flatTree(node)
  traverse(node)
  print("Done")

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

#       1
#    /    \
#   2      5
#  / \   /  \
# 3   4 6    7

t3n7 = Node(7, None, None)
t3n6 = Node(6, None, None)
t3n5 = Node(5, t3n6, t3n7)
t3n4 = Node(4, None, None)
t3n3 = Node(3, None, None)
t3n2 = Node(2, t3n3, t3n4)
t3n1 = Node(1, t3n2, t3n5)

#         1
#    /         \
#   2           5
#  / \         /  \
# 3   4       6    8
#      \     /
#       9   7

t4n9 = Node(9, None, None)
t4n8 = Node(8, None, None)
t4n7 = Node(7, None, None)
t4n6 = Node(6, t4n7, None)
t4n5 = Node(5, t4n6, t4n8)
t4n4 = Node(4, None, t4n9)
t4n3 = Node(3, None, None)
t4n2 = Node(2, t4n3, t4n4)
t4n1 = Node(1, t4n2, t4n5)

# 1
t5n1 = Node(1, None, None)

testNode(t1n1) #123
testNode(t2n1) #123456
testNode(t3n1) #1234567
testNode(t4n1) #123495678
testNode(t5n1) #1