# Given a binary tree, populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        h = self.getHeight(root)
        for i in range(h):
            Solution.nodes = []
            self.getLevelNode(root, i)
            for j in range(len(Solution.nodes)-1):
                Solution.nodes[j].next = Solution.nodes[j+1]
                

    def getLevelNode(self, root, level):
        if root == None:
            return
        if level == 0:
            Solution.nodes.append(root)
        elif level > 0:
            self.getLevelNode(root.left, level-1)
            self.getLevelNode(root.right, level-1)

    def getHeight(self, root):
        if root == None:
            return 0
        else:
            return max(self.getHeight(root.left), self.getHeight(root.right)) + 1
