# Rotate an array of n elements to the right by k steps.

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k %= l
        nums = nums[l-k:] + nums[:l-k]

        return nums

    def rotate2(self, nums, k):
        k %= len(nums)
        i = 0
        while i < k:
            nums.insert(0,nums.pop())
            i += 1

        return nums

if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    k = 3
    nums = Solution().rotate2(nums, k)
    print nums
    nums = [1,2]
    k = 1
    nums = Solution().rotate2(nums, k)
    print nums
