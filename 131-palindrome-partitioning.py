# Given a string s, partition s such that every substring of the partition is a palindrome.

# Return all possible palindrome partitioning of s.

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        Solution.ans = []
        self.dfs(s, [])
        return Solution.ans
    
    def dfs(self, s, strList):
        if len(s) == 0:
            Solution.ans.append(strList)
        for i in range(1, len(s)+1):
            if self.isPalindrome(s[:i]):
                self.dfs(s[i:], strList + [s[:i]])
            
    def isPalindrome(self, s):
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l +=1
            r -=1
        return True

if __name__ == "__main__":
    print Solution().partition("aaba")
