# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = str(self.getNumberFromListNode(l1) + self.getNumberFromListNode(l2))
        tmp = [int(x) for x in result]
        tmp.reverse()
        
        return tmp
        
    def getNumberFromListNode(self, current_node):
        result = []
        while current_node is not None:
            result.append(str(current_node.val))
            current_node = current_node.next
        result.reverse()
        return int(''.join(result))
