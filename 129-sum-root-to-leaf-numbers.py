# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

# An example is the root-to-leaf path 1->2->3 which represents the number 123.

# Find the total sum of all root-to-leaf numbers.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        pathList = self.findPath(root)
        pathList = map(int,pathList)
        return sum(pathList) 

    def findPath(self, root):
        if root == None:
            return ''
        if root.left == None and root.right == None:
            return str(root.val)
        pathList = [str(root.val) + path for path in self.findPath(root.left)]
        pathList += [str(root.val) + path for path in self.findPath(root.right)]
        return pathList

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print Solution().sumNumbers(root)
    root = TreeNode(1)
    root.left = TreeNode(0)
    print Solution().sumNumbers(root)
    root = TreeNode(4)
    root.left = TreeNode(9)
    root.right = TreeNode(0)
    root.left.left = TreeNode(1)
    print Solution().sumNumbers(root)
    
