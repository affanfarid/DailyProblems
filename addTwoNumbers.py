'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #add the first numbers, push the lowest digit to the list
        #take the remaining digit
        
        #create an empty linkedlist
        #initial addOn is 0
        
        finalListNode = new ListNode(0, None)
        addTwoNumsRecursive(l1, l2, finalListNode, 0)
        
        return finalListNode
        
        
    def addTwoNumsRecursive(self, l1, l2, finalListNode, addOn):
        
        if l1 == None and l2 == None:
            if addOn != 0:
                finalListNode.val = addOn
            return
        
        if l1 != None and l2 != None:
            tempSum = l1.val + l2.val + addOn
            onesPlace = tempSum %10
            tensPlace = tempSum //10
            
            finalListNode.val = onesPlace
            #fix
            finalListNode.next = ListNode(0, None)
            addTwoNumsRecursive(l1.next, l2.next, finalListNode.next, tensPlace)
            
        if l1 != None and l2 == None:
            tempSum = l1.val + addOn
            onesPlace = tempSum %10
            tensPlace = tempSum //10
            
            finalListNode.val = onesPlace
            #fix
            finalListNode.next = ListNode(0, None)
            addTwoNumsRecursive(l1.next, l2, finalListNode.next, tensPlace)
            
        if l1 == None and l2 != None:
            tempSum = l2.val + addOn
            onesPlace = tempSum %10
            tensPlace = tempSum //10
            
            finalListNode.val = onesPlace
            #fix
            finalListNode.next = ListNode(0, None)
            addTwoNumsRecursive(l1, l2.next, finalListNode.next, tensPlace)
            
        
        
