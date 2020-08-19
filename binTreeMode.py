'''
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than or equal to the node's key.
    The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
    Both the left and right subtrees must also be binary search trees.
'''
class Node:
  def __init__(self,value,left, right):
    self.value = value
    self.left = left
    self.right = right


def binTreeMode(node):
  numDict = {}
  binTreeModeRec(node,numDict)

  modeArr = []
  mode = 0
  for x in numDict:
    if numDict[x] > mode:
      modeArr = [x]
      mode = numDict[x]
    if numDict[x] == mode:
      modeArr += [x]

  return modeArr

def binTreeModeRec(node, numDict):
  if node.value in numDict:
    numDict[node.value] += 1
  else:
    numDict[node.value] = 1
    
  
  if node.left == None and node.right == None:
    return
  elif node.left == None:
    binTreeModeRec(node.right,numDict)
  elif node.right == None:
    binTreeModeRec(node.left,numDict)
  else:
    binTreeModeRec(node.left, numDict)
    binTreeModeRec(node.right, numDict)


