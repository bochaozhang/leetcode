# Given a binary tree, return the inorder traversal of its nodes' values.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        Nodes = []
        NodeVals = []
        current_node = root
        while current_node or len(Nodes):
            if current_node:
                Nodes.append(current_node)
                current_node = current_node.left
            else:
                current_node = Nodes.pop()
                NodeVals.append(current_node.val)
                current_node = current_node.right
        return NodeVals

if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print Solution().inorderTraversal(root)
