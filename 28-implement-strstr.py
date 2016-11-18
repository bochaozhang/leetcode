# Implement strStr().

# Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        import operator
        haystack = map(ord,haystack)
        needle = map(ord,needle)
        for i in range(len(haystack)-len(needle)+1):
            print haystack[i:i+len(needle)]
            print needle
            if map(operator.sub,haystack[i:i+len(needle)],needle) == [0]*len(needle):
                return i
        return -1

if __name__ == "__main__":
    print Solution().strStr('mississippi','pi')
