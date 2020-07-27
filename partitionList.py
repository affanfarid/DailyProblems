'''

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5



'''

'''
strat:
have a "separator pointer" which points to the division
and maybe one before that for all the nodes less than x

so lets do an example with the example Given

Input: head = 1->4->3->2->5->2, x = 3

sep = head at first
LTsep = head at first

now we traverse through the linked list

1 . 1 is less than 3, so we move sep to 1.next and LTsep is still at head.
4 . 4 is greater than 3 so we reposition 4 to be sep.next

----
strat2:
create 2 linked lists, one for greater than or equal to values, and one for less than
go through the org list, and sort them accordingly, moving the whole node

at the end, just combine the two lists 

'''

class Node:
  def __init__(self, value, nxt):
    self.value = value
    self.nxt = nxt

def arr2LinkedList(arr):
  if len(arr) == 0:
    return None
  head = Node(arr[0],None)
  temp = head
  for x in range(1,len(arr)):
    temp.nxt = Node(arr[x],None)
    temp = temp.nxt
  return head

def printLinkedList(head, name=None):
  print("-----")
  if name!=None:
    print(name)
  temp = head
  while temp != None:
    print(temp.value)
    temp = temp.nxt
  print("-----")

#IDEA WAS OVERDOING IT, SCRAPPED
def partList(head, x):
  #all values greater than or equal to x will be added to sep.nxt
  sep = head
  #all values less than x will be added to LTsep.nxt
  LTsep = head
  pointer = head
  #loop through list
  while pointer.nxt != None:
    #if the value is greater than or equal to x
    if pointer.value >= x:
      #saves rest of list starting node into temp
      temp = pointer.nxt
      #adds the node where it should be
      sep.nxt = pointer
      sep = sep.nxt
      sep.nxt = temp
      pointer = sep
    #if the value is less than x
    else:
      temp = pointer.nxt


      #return

#O(n) solution
def partList2(head,x):
  if head == None:
    return head
  
  pointer = head
  LThead = None
  LTtail = None
  GThead = None
  GTtail = None

  while pointer != None:
    #print("This node is: " + str(pointer.value))

    #this gets the remainder of the list 
    temp = pointer.nxt

    #node value is less than x
    if pointer.value < x:
      #if the LT list is empty
      if LThead == None:
        #moves the current node to the head of the list
        LThead = pointer
        LThead.nxt = None
        #sets the tail to the head since there is only one item in the list
        LTtail = LThead
      else:
        #adds the current node to end of list
        LTtail.nxt = pointer
        LTtail = LTtail.nxt
        #sets the end of list .next to None
        LTtail.nxt = None

    #node value is greater than x
    #exact same concept as the above if statement
    else:
      #if the GT list is currently empty
      if GThead == None:
        GThead = pointer
        GThead.nxt = None
        GTtail = GThead
      else:
        GTtail.nxt = pointer
        GTtail = GTtail.nxt
        GTtail.nxt = None
    
    #moves the pointer to the next node in the list
    pointer = temp 

  #combines the two lists and sets the head of the original list to the
  #head of the new combined list
  if LTtail == None:
    head = GThead
  else:
    LTtail.nxt = GThead
    head = LThead
  return head


test1 = [1,4,3,2,5,2]
test3 = []
test5 = [1,2,3,4,5,6]
test6 = [6,5,4,3,2,1]

printLinkedList(partList2(arr2LinkedList(test1),3),"test1")
printLinkedList(partList2(arr2LinkedList(test1),0),"test2")
printLinkedList(partList2(arr2LinkedList(test3),3),"test3")
printLinkedList(partList2(arr2LinkedList(test1),7),"test4")
printLinkedList(partList2(arr2LinkedList(test5),3),"test5")
printLinkedList(partList2(arr2LinkedList(test6),3),"test6")
