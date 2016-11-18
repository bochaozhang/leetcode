# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Defintion for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        n = len(lists)
        if n == 0:
            return None
        elif n == 1:
            return lists[0]
        elif n == 2:
            return self.mergeTwoLists(lists[0], lists[1])
        else:
            half = n / 2
            return self.mergeKLists([self.mergeKLists(lists[:half]), self.mergeKLists(lists[half:])])
       
    def mergeTwoLists(self, l1, l2):
        if l1 == None and l2 == None:
            return None
        dummy = ListNode(0)
        current_node = dummy
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                current_node.next = l1
                l1 = l1.next
                current_node = current_node.next
            else:
                current_node.next = l2
                l2 = l2.next
                current_node = current_node.next 
        if l1 != None:
            current_node.next = l1
        if l2 != None:
            current_node.next = l2
        return dummy.next

if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(3)
    l1.next.next = ListNode(5)
    l2 = ListNode(2)
    l2.next = ListNode(4)
    l2.next.next = ListNode(6)
    l3 = ListNode(7)
    l3.next = ListNode(8)
    l3.next.next = ListNode(9)
    ans = Solution().mergeKLists([l1, l2, l3])
    while ans != None:
        print ans.val
        ans = ans.next
