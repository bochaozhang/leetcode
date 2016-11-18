# Given a binary tree, find its maximum depth.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
     def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        else:
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
            return max(left_depth,right_depth) + 1

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(1)
    root.right.right = TreeNode(0) 
    print Solution().maxDepth(root)
