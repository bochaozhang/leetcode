# Given preorder and inorder traversal of a tree, construct the binary tree.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0 or len(inorder) == 0:
            return []
        root = TreeNode(0)
        Solution.preorder = list(preorder)
        self.createTree(root, inorder)
        return root

    def createTree(self, root, inorder):
        root.val = Solution.preorder[0]
        p = inorder.index(root.val)
        if p > 0:
            root.left = TreeNode(0)
            left_inorder = inorder[0:p]
            Solution.preorder.remove(Solution.preorder[0])
            self.createTree(root.left, left_inorder)
        if p < len(inorder)-1:
            root.right = TreeNode(0)
            right_inorder = inorder[p+1:len(inorder)]
            Solution.preorder.remove(Solution.preorder[0])
            self.createTree(root.right, right_inorder)

    def preorderTraverse(self, root):
        if root:
            print root.val
            self.preorderTraverse(root.left)
            self.preorderTraverse(root.right)

    def inorderTraverse(self, root):
        if root:
            self.inorderTraverse(root.left)
            print root.val
            self.inorderTraverse(root.right)        

if __name__ == "__main__":
    root = Solution().buildTree("ABDHLEKCFG","HLDBEKAFCG")
    Solution().preorderTraverse(root)
    Solution().inorderTraverse(root)
