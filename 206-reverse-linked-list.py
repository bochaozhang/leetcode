# Reverse a singly linked list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        current_node = head.next
        head.next = None
        while (current_node != None):
            next_node = current_node.next
            current_node.next = head
            head = current_node
            current_node = next_node
        return head
