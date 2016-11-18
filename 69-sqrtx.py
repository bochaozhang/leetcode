# Implement int sqrt(int x).

#Compute and return the square root of x.

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return None
        if x == 0:
            return 0
        if x == 1:
            return 1
        left = 0
        right = x
        while left <= right:
            mid = (left + right) / 2
            print [left, right, mid]
            if x / mid == mid:
                return mid
            elif x / mid > mid:
                left = mid + 1
            elif x / mid < mid:
                right = mid - 1
        return right               

if __name__ == "__main__":
    print Solution().mySqrt(5)
    print Solution().mySqrt(15)
    print Solution().mySqrt(25)
