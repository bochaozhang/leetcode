# Given a string, find the length of the longest substring without repeating characters. 

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        cur = -1
        dict = {}
        for i in xrange(len(s)):
            if s[i] in dict:
                cur = max(dict[s[i]],cur)
            longest = max(longest,i-cur)
            dict[s[i]] = i
        return longest

if __name__ == "__main__":
    print Solution().lengthOfLongestSubstring("")
    print Solution().lengthOfLongestSubstring("c")
    print Solution().lengthOfLongestSubstring("aab")
    print Solution().lengthOfLongestSubstring("abbcabcbb")
    print Solution().lengthOfLongestSubstring("bbbbb")
