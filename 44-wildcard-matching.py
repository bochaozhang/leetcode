# Implement wildcard pattern matching with support for '?' and '*'.

# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).

class Solution(object):
    def isMatch_recur(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) == 0:
            return len(s) == 0
        elif len(p) == 1:
            if p[0] == '*': 
                return True
            else:
                if len(s) != 1: 
                    return False
                else:
                    return p[0] == '?' or p[0] == s[0] 
        else:
            if p[0] == '?':
                if len(s) < 1: return False
                return self.isMatch(s[1:], p[1:])
            elif p[0] == '*':
                for i in range(len(s)):
                    if self.isMatch(s[i:], p[1:]):
                        return True
                return False
            else:
                if len(s) < 1: return False
                if p[0] != s[0]: 
                    return False
                else: 
                    return self.isMatch(s[1:], p[1:])

    def isMatch(self, s, p):
        len_s, len_p = len(s), len(p)
        pPointer = sPointer = aPointer = 0
        asterick = -1
        while sPointer < len_s:
            if pPointer < len_p and (p[pPointer] == '?' or p[pPointer] == s[sPointer]):
                sPointer += 1; pPointer += 1
                continue
            if pPointer < len_p and p[pPointer] == '*':
                asterick = pPointer; pPointer += 1; aPointer = sPointer
                continue
            if asterick != -1:
                pPointer = asterick + 1; aPointer += 1; sPointer = aPointer
                continue
            return False
        while pPointer < len_p and p[pPointer] == '*':
            pPointer += 1
        return pPointer == len_p
               
if __name__ == "__main__":
    print Solution().isMatch("aa", "a") 
    print Solution().isMatch("aa", "aa") 
    print Solution().isMatch("aaa", "aa") 
    print Solution().isMatch("aa", "*") 
    print Solution().isMatch("aa", "a*") 
    print Solution().isMatch("ab", "?*") 
    print Solution().isMatch("aab", "c*a*b") 
    print Solution().isMatch("aa", "a*") 
    print Solution().isMatch("a", "a*") 
