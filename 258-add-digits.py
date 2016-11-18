# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        else:
            if num % 9 == 0:
                return 9
            else:
                return num % 9

if __name__ == "__main__":
    print Solution().addDigits(38)
    print Solution().addDigits(1853)
    print Solution().addDigits(0)
    print Solution().addDigits(18)
