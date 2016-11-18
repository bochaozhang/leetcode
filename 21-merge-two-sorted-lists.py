# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None: return l2
        if l2 == None: return l1
        head = None
        while (l1 != None and l2 != None):
            if l1.val <= l2.val:
                current_node = ListNode(l1.val)
                current_node.next = head
                head = current_node
                l1 = l1.next
            else:
                current_node = ListNode(l2.val)
                current_node.next = head
                head = current_node
                l2 = l2.next
        while (l1 != None):
            current_node = ListNode(l1.val)
            current_node.next = head
            head = current_node
            l1 = l1.next
        while (l2 != None):
            current_node = ListNode(l2.val)
            current_node.next = head
            head = current_node
            l2 = l2.next
        head = self.reverseList(head)
        return head

    def reverseList(self, head):
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
 

if __name__ == "__main__":
    a = ListNode(1)
    a.next = ListNode(3)
    b = ListNode(2)
    b.next = ListNode(4)
    merged = Solution().mergeTwoLists(a,b)
    while merged != None:
        print merged.val
        merged = merged.next
