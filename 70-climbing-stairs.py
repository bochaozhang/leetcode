# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        step1 = 1
        step2 = 2
        
        if n==1:
            return step1
        elif n==2:
            return step2
        else:
            for i in range(3,n+1):
                temp = step1 + step2
                step1 = step2
                step2 = temp
            return temp

if __name__ == "__main__":
    print Solution().climbStairs(1) 
    print Solution().climbStairs(2) 
    print Solution().climbStairs(3) 
    print Solution().climbStairs(4) 
    print Solution().climbStairs(5) 
