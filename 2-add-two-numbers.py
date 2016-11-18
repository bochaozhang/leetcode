# You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s = ListNode(0)
        dummy = s
        carry = 0
        while (l1 != None and l2 != None):
            s.next = ListNode((l1.val + l2.val + carry) % 10)
            if l1.val + l2.val + carry >= 10:
                carry = 1
            else:
                carry = 0
            l1 = l1.next
            l2 = l2.next
            s = s.next
        while (l1 != None):
            s.next = ListNode((l1.val + carry) % 10)
            if l1.val + carry >= 10:
                carry = 1
            else:
                carry = 0
            l1 = l1.next
            s = s.next
        while (l2 != None):
            s.next = ListNode((l2.val + carry) % 10)
            if l2.val + carry >= 10:
                carry = 1
            else:
                carry = 0
            l2 = l2.next
            s = s.next
        if carry == 1:
            s.next = ListNode(1)
        return dummy.next

if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(5)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    l2.next.next.next = ListNode(9)
    s = Solution().addTwoNumbers(l1,l2)
    while (s != None):
        print s.val
        s = s.next        
