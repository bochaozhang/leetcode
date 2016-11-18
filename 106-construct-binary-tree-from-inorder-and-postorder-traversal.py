# Given inorder and postorder traversal of a tree, construct the binary tree.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(postorder) == 0 or len(inorder) == 0:
            return []
        root = TreeNode(0)
        Solution.postorder = list(postorder)
        self.createTree(root, inorder)
        return root

    def createTree(self, root, inorder):
        root.val = Solution.postorder[-1]
        p = inorder.index(root.val)
        if p < len(inorder)-1:
            root.right = TreeNode(0)
            right_inorder = inorder[p+1:len(inorder)]
            Solution.postorder.remove(Solution.postorder[-1])
            self.createTree(root.right, right_inorder)
        if p > 0:
            root.left = TreeNode(0)
            left_inorder = inorder[0:p]
            Solution.postorder.remove(Solution.postorder[-1])
            self.createTree(root.left, left_inorder)

    def postorderTraverse(self, root):
        if root:
            self.postorderTraverse(root.left)
            self.postorderTraverse(root.right)
            print root.val

    def inorderTraverse(self, root):
        if root:
            self.inorderTraverse(root.left)
            print root.val
            self.inorderTraverse(root.right)        

if __name__ == "__main__":
    root = Solution().buildTree("HLDBEKAFCG", "LHDKEBFGCA")
    Solution().inorderTraverse(root)
    Solution().postorderTraverse(root)
