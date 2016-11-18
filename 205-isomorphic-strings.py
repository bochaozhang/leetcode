# Given two strings s and t, determine if they are isomorphic.

# Two strings are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic1 = {}
        dic2 = {}
        for i in range(len(s)):
            if s[i] not in dic1:
                dic1[s[i]] = t[i]
            if s[i] in dic1:
                if dic1[s[i]] != t[i]:
                    return False
            if t[i] not in dic2:
                dic2[t[i]] = s[i]
            if t[i] in dic2:
                if dic2[t[i]] != s[i]:
                    return False
        return True

if __name__ == "__main__":
    print Solution().isIsomorphic("","")
    print Solution().isIsomorphic("egg","add")
    print Solution().isIsomorphic("foo","bar")
    print Solution().isIsomorphic("bar","foo")
    print Solution().isIsomorphic("paper","title")
