# Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.

# Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        if len(preorder) == 0:
            return False;
        nodes = preorder.split(",")
        diff = 1
        for i in range(0,len(nodes)):
            diff -= 1
            if diff < 0:
                return False
            if nodes[i] != "#":
                diff +=2
        return diff == 0

if __name__ == "__main__":
    print Solution().isValidSerialization("")
    print Solution().isValidSerialization("#")
    print Solution().isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")
    print Solution().isValidSerialization("1,#")
    print Solution().isValidSerialization("9,#,#,1")
        
