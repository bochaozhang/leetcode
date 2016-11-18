# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        h = self.getHeight(root)
        ans = []
        for i in range(h):
            Solution.nodes = []
            self.getLevelNode(root, i)
            if i % 2 == 0:
                ans.append(Solution.nodes)
            else:
                ans.append(Solution.nodes[::-1])
        return ans

    def getLevelNode(self, root, level):
        if root == None:
            return
        if level == 0:
            Solution.nodes.append(root.val)
        elif level > 0:
            self.getLevelNode(root.left, level-1)
            self.getLevelNode(root.right, level-1)
            
    def getHeight(self, root):
        if root == None:
            return 0
        else:
            return max(self.getHeight(root.left), self.getHeight(root.right)) + 1

if __name__ == "__main__":
    head = TreeNode(3)
    head.left = TreeNode(9)
    head.right = TreeNode(20)
    head.right.left = TreeNode(15)
    head.right.right = TreeNode(7)
    print Solution().zigzagLevelOrder(head) 
