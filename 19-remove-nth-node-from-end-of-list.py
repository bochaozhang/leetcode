# Given a linked list, remove the nth node from the end of list and return its head.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n == 0 or head == None:
            return None
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        p = q = head
        for i in range(n+1):
            if q != None:
                q = q.next
            else:
                return None
        while q != None:
            p = p.next
            q = q.next
        p.next = p.next.next
        return head.next

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    ans = Solution().removeNthFromEnd(head, 2)
    while ans != None:
        print ans.val
        ans = ans.next
