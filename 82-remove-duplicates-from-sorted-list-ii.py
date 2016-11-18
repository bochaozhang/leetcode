# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

# Definition for singly-linked list.
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
        dummy = ListNode(0)
        dummy.next = head
        previous_node = dummy
        current_node = head
        duplicates = []
        while current_node:
            if current_node.next and current_node.val == current_node.next.val:
                current_node.next = current_node.next.next
                duplicates.append(current_node.val)
            elif current_node.val in duplicates:
                previous_node.next = current_node.next
                current_node = previous_node.next
                duplicate = False
            else:
                current_node = current_node.next
                previous_node = previous_node.next
        return dummy.next

    def createList(self, nums):
        current_node = head = ListNode(0)
        for i in range(len(nums)):
            current_node.next = ListNode(nums[i])
            current_node = current_node.next
        return head.next

    def printList(self, head):
        while head:
            print head.val
            head = head.next

if __name__ == "__main__":
    head = Solution().createList([1,1,2,3,3,4,4,5,5])
    head = Solution().deleteDuplicates(head)
    Solution().printList(head)
    
            
