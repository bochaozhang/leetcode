# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxWater = 0
        maxL = 0
        maxR = 0
        l, r = 0, len(height)-1
        while l < r:
            if height[l] > maxL or height[r] > maxR:
                maxL = max(height[l],maxL)
                maxR = max(height[r],maxR)
                water = min(height[l],height[r]) * (r-l)
                if water > maxWater:
                    maxWater = water
            if height[l] >= height[r]:
                r -= 1 
            elif height[l] < height[r]:
                l += 1
        return maxWater

if __name__ == "__main__":
    print Solution().maxArea([1,2,3,4,5])
    print Solution().maxArea([1,2,3,4,5,6])
