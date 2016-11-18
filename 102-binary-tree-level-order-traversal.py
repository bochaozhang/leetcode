# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        h = self.height(root)
        ans = [[] for x in range(h)]
        self.levelNode(root, h-1, ans)
        return ans[::-1]

    def levelNode(self, root, level, ans):
        if root == None:
            return        
        ans[level].append(root.val)
        self.levelNode(root.left, level-1, ans)
        self.levelNode(root.right, level-1, ans)

    def height(self, root):
        if root == None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print Solution().levelOrder(root)
