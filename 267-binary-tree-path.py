# Given a binary tree, return all root-to-leaf paths.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root == None:
            return []
        if root.left == None and root.right == None:
            return [str(root.val)]
        pathList = [str(root.val) + '->' + path for path in self.binaryTreePaths(root.left)] 
        pathList += [str(root.val) + '->' + path for path in self.binaryTreePaths(root.right)]
        return pathList

if __name__ == "__main__":
    print Solution().binaryTreePaths([])
