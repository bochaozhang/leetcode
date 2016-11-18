# Determine whether an integer is a palindrome. Do this without extra space.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        forward = x
        backward = 0
        while x > 0:
            backward = backward * 10 + x % 10
            x /= 10
        return backward == forward

if __name__ == "__main__":
    print Solution().isPalindrome(123)  
    print Solution().isPalindrome(-123)  
    print Solution().isPalindrome(101)  
    print Solution().isPalindrome(-101)  
