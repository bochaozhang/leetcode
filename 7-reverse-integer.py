# Reverse digits of an integer.

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        p = 1
        if x < 0:
            p = -1
            x = -1 * x
        x = str(x)
        x = x[::-1]
        x = int(x)
        if x > 2147483647:
            x = 0
        return x * p

if __name__ == "__main__":
    print Solution().reverse(-123)
    print Solution().reverse(-100)
    print Solution().reverse(1000000003)
