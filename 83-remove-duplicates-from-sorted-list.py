# Given a sorted linked list, delete all duplicates such that each element appear only once.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        current_node = head
        next_node = head.next
        while next_node != None:
            if current_node.val == next_node.val:
                current_node.next = next_node.next
                next_node = next_node.next
            else:
                current_node = current_node.next
                next_node = next_node.next
        return head

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(3)
    head.next.next.next.next.next = ListNode(3)
    head = Solution().deleteDuplicates(head)
    while head:
        print head.val
        head = head.next
