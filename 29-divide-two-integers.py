# Divide two integers without using multiplication, division and mod operator.

# If it is overflow, return MAX_INT.

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # determine sign of quotient
        p = 1
        if dividend < 0:
            dividend = -dividend
            p = -p
        if divisor < 0:
            divisor = -divisor
            p = -p
        Solution.divisor = divisor
        if p > 0:
            return min(self.division(dividend, divisor), 2147483647)
        else:
            return max(0 - self.division(dividend, divisor), -2147483648)
    
    def division(self, dividend, tempDivisor):
        if dividend == tempDivisor:
            return 1
        if dividend < tempDivisor:
            return 0
        # align divisor and divident
        quotient = 1
        while tempDivisor << 1 <= dividend:
            tempDivisor = tempDivisor << 1
            quotient = quotient << 1
        quotient += self.division(dividend - tempDivisor, Solution.divisor)
        return quotient

if __name__ == "__main__":
    print Solution().divide(15, 3)        
    print Solution().divide(15, -7)        
