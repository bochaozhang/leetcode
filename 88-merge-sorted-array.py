# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        idx = m + n -1
        i = m - 1
        j = n - 1
        while idx >= 0 and i >= 0 and j>= 0:
            if nums1[i] >= nums2[j]:
                nums1[idx] = nums1[i]
                i -= 1
                idx -= 1
            if nums1[i] < nums2[j]:
                nums1[idx] = nums2[j]
                j -= 1
                idx -= 1
        if j >= 0:
            nums1[:j+1] = nums2[:j+1]
        return nums1

if __name__ == "__main__":
    print Solution().merge([1,3,5,0,0], 3, [2,4], 2)
    print Solution().merge([1], 1, [], 0)
    print Solution().merge([0], 0, [1], 1)
    print Solution().merge([1,2,3,0,0,0], 3, [2,5,6], 3)
    print Solution().merge([11,12,13,0,0,0], 3, [2,5,6], 3)
