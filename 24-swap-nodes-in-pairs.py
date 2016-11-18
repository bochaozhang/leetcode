# Given a linked list, swap every two adjacent nodes and return its head.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == []:
            return []
        dummy = ListNode(0)
        dummy.next = head
        current_node = dummy
        while current_node != None and current_node.next != None and current_node.next.next != None:
            next_node = current_node.next
            current_node.next = next_node.next
            next_node.next = current_node.next.next
            current_node.next.next = next_node
            current_node = next_node
        return dummy.next
            

if __name__ == "__main__":
    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(3)
    root.next.next.next = ListNode(4)
    root.next.next.next.next = ListNode(5)
    root = Solution().swapPairs(root)
    while root != None:
        print root.val
        root = root.next        
