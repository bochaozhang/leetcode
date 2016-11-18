# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        letters = re.compile("[^a-zA-Z0-9]")
        s = letters.sub('',s)
        s = s.lower() 
        return s == s[::-1]
                
if __name__ == "__main__":
    print Solution().isPalindrome("")
    print Solution().isPalindrome("A man, a plan, a canal: Panama")
