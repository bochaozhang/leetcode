# Given a binary tree, determine if it is a valid binary search tree (BST).

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        maxKey = pow(2,31) - 1
        minKey = -maxKey
        return self.isValid(root, minKey+1, maxKey-1)

    def isValid(self, root, minKey, maxKey):
        if root == None: return True
        if root.val < minKey or root.val > maxKey: return False
        return self.isValid(root.left, minKey, root.val) and self.isValid(root.right, root.val, maxKey)

if __name__ == "__main__":
    
