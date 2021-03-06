# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(0)
        head = l3
        if l2 == None:
            return l1
            
        if l1 == None:
            return l2
        while l1 != None and l2 != None:
            if l1.val >= l2.val:
                l3.next = l2
                l2 = l2.next
            else:
                l3.next = l1
                l1 = l1.next
                
            l3 = l3.next
            
        if l1 == None:
            l3.next = l2
        if l2 == None:
            l3.next = l1
            
        return head.next