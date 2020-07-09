'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.

'''





class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def removeNode(n, head):
  slowPointer = head
  fastPointer = head

  #sets fast pointer 2 steps ahead of slow pointer
  for x in range(0,n):
    fastPointer = fastPointer.next

  # while(True):
  #   if fastPointer.next = None:
  #     #delete slowPointer
  #     return
  #   else:
  #     fastPointer = fastPointer.next
  #     slowPointer = slowPointer.next

  while(True):
    if fastPoint.next.next == None:
      temp = slowPointer.next.next
      del slowPointer.next 
      slowPointer.next = temp 
      return head
    else:
      fastPointer = fastPointer.next
      slowPointer = slowPointer.next




