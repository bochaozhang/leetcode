# Implement pow(x, n).

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n > 0:
            return self.power(x,n)
        if n < 0:
            return float(1) / self.power(x,-n)

    def power(self, x, n):
        if n == 1:
            return x
        if n % 2 == 0:
            r = self.power(x,n/2)
            return r * r
        if n % 2 == 1:
            r = self.power(x,n/2)
            return r * r * x

if __name__ == "__main__":
    print Solution().myPow(3.12,5)
