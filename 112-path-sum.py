# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        sum -= root.val
        if root.left == None and root.right == None:
            return sum == 0
        if root.left and self.hasPathSum(root.left, sum):
            return True
        if root.right and self.hasPathSum(root.right, sum): 
            return True
        return False   

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    print Solution().hasPathSum(root, 6)
    print Solution().hasPathSum(root, 7)
    print Solution().hasPathSum(root, 8)
