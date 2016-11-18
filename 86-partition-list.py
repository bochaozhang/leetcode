# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        lesser = ListNode(0)
        lesser_current = lesser
        dummy = ListNode(0)
        dummy.next = head
        current_node = dummy
        while current_node.next:
            if current_node.next.val < x:
                lesser_current.next = ListNode(current_node.next.val)
                lesser_current = lesser_current.next
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
        lesser_current.next = dummy.next
        return lesser.next
    
    def makeList(self, nodes):
        head = current_node = ListNode(nodes[0])
        for i in range(1,len(nodes)):
            current_node.next = ListNode(nodes[i])
            current_node = current_node.next
        return head

    def printList(self, head):
        while head:
            print head.val
            head = head.next
        return None

if __name__ == "__main__":
    head = Solution().makeList([1,4,3,2,5,2])
    head = Solution().partition(head,3)
    Solution().printList(head)
