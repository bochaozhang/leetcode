# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left_top = [0] * n
        for i in range(1,n):
            left_top[i] = max(height[i-1],left_top[i-1])
        right_top = [0] * n
        for i in range(n-2,-1,-1):
            right_top[i] = max(height[i+1],right_top[i+1])
        ans = 0
        for i in range(n):
            ans += max(min(left_top[i],right_top[i])-height[i],0)
        return ans

if __name__ == "__main__":
    print Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])
                
