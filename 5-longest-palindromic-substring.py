# Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s
        ans = ''
        for i in range(len(s)):
            string = self.palindrome(s,i,i)
            if len(string) > len(ans):
                 ans = string
            string = self.palindrome(s,i,i+1)
            if len(string) > len(ans):
                ans = string
        return ans         

    def palindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]                    

if __name__ == "__main__":
    print Solution().longestPalindrome("dabad")
    print Solution().longestPalindrome("tabad")
